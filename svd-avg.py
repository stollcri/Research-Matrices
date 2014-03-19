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


def multiply_matrices(matrixU, matrixS, matrixVt, kmin, kmax, depth, rescale=False, contrast=False):
	matrixScopy = matrixS.copy()

	# when kmax is not 0 use the provided kmax
	if kmax > 0:
		i = 0
		contrast_factor = (1.0 + (1 - (math.log(kmax, 2) / 10)))
		for t in numpy.nditer(matrixScopy, op_flags=["readwrite"]):
			if i < kmin or i >= kmax:
				t[...] = 0
			else:
				if contrast:
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
	if rescale:
		curMin = 0
		curMax = 0
		# find min and max values
		for n in numpy.nditer(matrixComposed):
			if int(round(n)) < curMin:
				curMin = int(round(n))
			if int(round(n)) > curMax:
				curMax = int(round(n))
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

	if contrast:
		depth_limit = depth # int(depth - (depth * .01))
		for t in numpy.nditer(matrixComposed, op_flags=["readwrite"]):
			if t < depth_limit:
				t[...] = 0

	return matrixComposed


def write_matrices_to_file(matrixU, matrixS, matrixVt, kmin, kmax, width, height, depth, filename, rescale=False, contrast=False):
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
	A = multiply_matrices(matrixU, matrixS, matrixVt, kmin, kmax, depth, rescale, contrast)

	pixelate_count = 4
	for x in xrange(1, pixelate_count):
		U, s, Vt = numpy.linalg.svd(A, full_matrices=True)
		A = multiply_matrices(U, s, Vt, kmin, kmax, depth, rescale, contrast)

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
		if png_image.mode == 'L':
			pixelr = pixel
		elif png_image.mode == 'RGB':
			pixelr, pixelg, pixelb = pixel
		elif png_image.mode == 'RGBA':
			pixelr, pixelg, pixelb, pixela = pixel
		image.matrix[row][col] = int(pixelr)
		col += 1
	
	# # columns which are all black become all white
	# for x in xrange(0, image.width):
	# 	colnull = True
	# 	for y in xrange(0, image.height):
	# 		if int(image.matrix[y][x]) != 0:
	# 			colnull = False
	# 	if colnull:
	# 		for y in xrange(0, image.height):
	# 			image.matrix[y][x] = image.depth

	return image
	

def process_svd(source_file_a, source_file_b, destination_file, kmin, kmax, rescale, contrast):
	"""
	Read from file provided on the command line or from stdin
	then save uncompressed representations of the SVD compressed version
	"""
	"""
	imagea = read_matrix_from_file(source_file_a)
	Ma = numpy.asmatrix(imagea.matrix)
	U, s, Vt = numpy.linalg.svd(Ma, full_matrices=True)
	"""
	pixelate_count = 2 + int(kmax / 2)

	imagea = read_matrix_from_file(source_file_a)
	Ma = numpy.asmatrix(imagea.matrix)
	# for x in xrange(1, pixelate_count):
	# 	Ua, sa, Vta = numpy.linalg.svd(Ma, full_matrices=True)
	# 	Ma = multiply_matrices(Ua, sa, Vta, kmin, kmax, imagea.depth, rescale, contrast)
	Ua, sa, Vta = numpy.linalg.svd(Ma, full_matrices=True)

	imageb = read_matrix_from_file(source_file_b)
	Mb = numpy.asmatrix(imageb.matrix)
	for x in xrange(1, pixelate_count):
		Ub, sb, Vtb = numpy.linalg.svd(Mb, full_matrices=True)
		Mb = multiply_matrices(Ub, sb, Vtb, kmin, kmax, imageb.depth, rescale, contrast)

	U = Ua
	for (x,y), value in numpy.ndenumerate(Ua):
		inta = Ua[x, y]
		intb = Ub[x, y]
		#intc = ((inta * 1.618) + (intb * 0.3)) / 1.9
		#intc = (inta + intb) / 2.0
		#intc = ((inta * 2) + intb) / 3.0
		#intc = ((inta * 3) + intb) / 4.0
		#intc = ((inta * 4) + intb) / 5.0
		intc = ((inta * 5) + intb) / 6.0
		#intc = ((inta * 6) + intb) / 7.0
		#intc = ((inta * 7) + intb) / 8.0
		U[x, y] = intc

	s = sa
	for (x,), value in numpy.ndenumerate(sa):
		inta = sa[x]
		intb = sb[x]
		#intc = ((inta * 1.618) + (intb * 0.3)) / 1.9
		#intc = (inta + intb) / 2.0
		#intc = ((inta * 2) + intb) / 3.0
		#intc = ((inta * 3) + intb) / 4.0
		#intc = ((inta * 4) + intb) / 5.0
		intc = ((inta * 5) + intb) / 6.0
		#intc = ((inta * 6) + intb) / 7.0
		#intc = ((inta * 7) + intb) / 8.0
		s[x] = intc

	Vt = Vta
	for (x,y), value in numpy.ndenumerate(Vta):
		inta = Vta[x, y]
		intb = Vtb[x, y]
		#intc = ((inta * 1.618) + (intb * 0.3)) / 1.9
		#intc = (inta + intb) / 2.0
		#intc = ((inta * 2) + intb) / 3.0
		#intc = ((inta * 3) + intb) / 4.0
		#intc = ((inta * 4) + intb) / 5.0
		intc = ((inta * 5) + intb) / 6.0
		#intc = ((inta * 6) + intb) / 7.0
		#intc = ((inta * 7) + intb) / 8.0
		Vt[x, y] = intc
	
	write_matrices_to_file(U, s, Vt, kmin, kmax, imagea.width, imagea.height, imagea.depth, destination_file, rescale, contrast)



if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("infile1", nargs='?', help="The source ASCII PGM file", type=argparse.FileType('r'), default=sys.stdin)
	parser.add_argument("infile2", nargs='?', help="The source ASCII PGM file", type=argparse.FileType('r'), default=sys.stdin)
	parser.add_argument("outfile", nargs='?', help="The destination ASCII PGM file", type=argparse.FileType('w'), default=sys.stdout)
	parser.add_argument("-j", "--kmin", help="The number of high k values to exlude", type=int, default=0)
	parser.add_argument("-k", "--kmax", help="The number k values to use", type=int, default=0)
	parser.add_argument("-s", "--scale", help="Fit resulting image depth into '0 < n < depth' bounds", action="store_true")
	parser.add_argument("-c", "--contrast", help="Improve high contrast images", action="store_true")
	args = parser.parse_args()

	try:
		process_svd(args.infile1, args.infile2, args.outfile, args.kmin, args.kmax, args.scale, args.contrast)
	except KeyboardInterrupt:
		exit(0)
