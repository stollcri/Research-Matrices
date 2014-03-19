#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import argparse
import numpy
import math
from PIL import Image

class SVDimage:
	def __init__(self, matrix=[[]], width=0, height=0, depth=0):
		self.matrix = matrix
		self.width = width
		self.height = height
		self.depth = depth

	def set_width_and_height(self, width, height):
		self.width = width
		self.height = height
		self.matrix = [[0 for j in xrange(height)] for i in xrange(width)]


def multiply_matrices(matrixU, matrixS, matrixVt, kmin, kmax, depth):
	matrixScopy = matrixS.copy()

	# when kmax is not 0 use the provided kmax
	if kmax > 0:
		i = 0
		contrast_factor = (1.0 + (1 - (math.log(kmax, 2) / 10)))
		for t in numpy.nditer(matrixScopy, op_flags=["readwrite"]):
			if i < kmin or i >= kmax:
				t[...] = 0
			else:
				t[...] = t * contrast_factor #* math.pi / 2
			i += 1
	# when kmax is 0 then drop eigen values less than 1.0E-14
	else:
		for t in numpy.nditer(matrixScopy, op_flags=["readwrite"]):
			if round(t, 14) <= 0:
				t[...] = 0
	
	# recompose the trimmed SVD matrices back into matrix matrixComposed
	matrixComposed = numpy.dot(numpy.dot(matrixU, numpy.diag(matrixScopy)), matrixVt)

	# attempt the handle out of range values (TODO: pull out to own function)
	curMin = 0
	curMax = 0
	# find min and max values
	for n in numpy.nditer(matrixComposed):
		if int(round(n)) < curMin:
			curMin = int(round(n))
		if int(round(n)) > curMax:
			curMax = int(round(n))
	# catch some extreme values
	# if (curMax - curMin) > (depth * 10):
	# 	print "Whoa:", curMax, curMin
	# 	for t in numpy.nditer(matrixComposed, op_flags=["readwrite"]):
	# 		if t > (depth * 10):
	# 			t[...] = (depth * 10)
	# 		elif t < (depth * -10):
	# 			t[...] = (depth * -10)
	# shift values up
	if curMax < depth and curMin < 0:
		shiftVal = depth - curMax
		for t in numpy.nditer(matrixComposed, op_flags=["readwrite"]):
			t[...] = int(round(t + shiftVal))
			if t > depth:
				t[...] = depth
			elif t < 0:
				t[...] = 0
	# shift values down
	elif curMax > depth and curMin > 0:
		shiftVal = curMin
		for t in numpy.nditer(matrixComposed, op_flags=["readwrite"]):
			t[...] = int(round(t - shiftVal))
			if t > depth:
				t[...] = depth
			elif t < 0:
				t[...] = 0
	# no chance to shift, just chop (TODO: perform some sort of scaling)
	else:
		for t in numpy.nditer(matrixComposed, op_flags=["readwrite"]):
			t[...] = int(round(t))
			if t > depth:
				t[...] = depth
			elif t < 0:
				t[...] = 0

	depth_limit = depth # int(depth - (depth * .01))
	for t in numpy.nditer(matrixComposed, op_flags=["readwrite"]):
		if t < depth_limit:
			t[...] = 0

	return matrixComposed


def write_matrices_to_file(matrixU, matrixS, matrixVt, kmin, kmax, width, height, depth, filename):
	"""
	Write a decomposed matrix to file uncompressed as it would show compressed

	Keyword Arguments:
	matrixU -- the U portion of the SVD
	matrixS -- the S (sigma) portion of the SVD
	matrixVt -- the V transpose portion of the SVD
	kmin -- the minimum k value to use for compresion (ignored if kmax = 0)
	kmax -- the maximum kvalue to use for compresion (find optimal if zero)
	filename -- the file to write to (stdout if blank)
	width -- the image width
	height -- the image height
	depth -- the maximum grey scale value (normally 255)
	rescale -- True to shift resulting image into 0 < n < depth bounds
	"""
	A = multiply_matrices(matrixU, matrixS, matrixVt, kmin, kmax, depth)
	
	pixelate_count = 2 + int(kmax / 2)
	for x in xrange(1, pixelate_count):
		Utmp, stmp, Vttmp = numpy.linalg.svd(A, full_matrices=True)
		A = multiply_matrices(Utmp, stmp, Vttmp, kmin, kmax, depth)

	png_image = Image.new('L', (width, height))
	for i in xrange(0, width):
		for j in xrange(0, height):
			pixelval = int(A[j, i])
			png_image.putpixel((i, j), pixelval)
	png_image.save(filename)


def read_matrix_from_file(filename):
	"""
	Read a PNG file and create an Image object from it
	"""
	png_image = Image.open(filename)
	png_image.thumbnail((64, 64), Image.ANTIALIAS)

	image = SVDimage()
	image.depth = 255
	width, height = png_image.size
	image.set_width_and_height(width, height)

	row = 0
	col = 0
	for pixel in list(png_image.getdata()):
		if col >= image.width:
			row += 1
			col = 0
		# TODO: something better than taking the red value
		if len(pixel) == 3:
			pixelr, pixelg, pixelb = pixel
		elif len(pixel) == 4:
			pixelr, pixelg, pixelb, pixela = pixel
		image.matrix[row][col] = int(pixelr)
		col += 1
	
	return image
	

def process_svd(source_file, destination_file, kmin, kmax):
	"""
	Read from file provided on the command line or from stdin
	then save uncompressed representations of the SVD compressed version
	"""
	image = read_matrix_from_file(source_file)

	M = numpy.asmatrix(image.matrix)
	U, s, Vt = numpy.linalg.svd(M, full_matrices=True)
	
	write_matrices_to_file(U, s, Vt, kmin, kmax, image.width, image.height, image.depth, destination_file)



if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("infile", nargs='?', help="The source ASCII PGM file", type=argparse.FileType('r'), default=sys.stdin)
	parser.add_argument("outfile", nargs='?', help="The destination ASCII PGM file", type=argparse.FileType('w'), default=sys.stdout)
	parser.add_argument("-j", "--kmin", help="The number of high k values to exlude", type=int, default=0)
	parser.add_argument("-k", "--kmax", help="The number k values to use", type=int, default=0)
	args = parser.parse_args()

	try:
		process_svd(args.infile, args.outfile, args.kmin, args.kmax)
	except KeyboardInterrupt:
		exit(0)
