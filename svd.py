#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This program is for learning purposes, it doesn't do anything useful outside of aiding in learning SVD.

The program takes an PNG file, converts it into a matrix, runs SVD on it, removes eigenvalues above
some k value (and optionally below some j value), and then outputs a PNG file of the resulting compressed
image. It is important to note that the image is not really compressed further, it shows what an equivalent
SVD based compresion for the given k values would look like. It's a visual aid to learning SVD compresion.

The SVD process can result in values above the PNG greyscale limit and below zero, so there is a scale option
which will attempt to bring the resulting image within the bounds of 0 and 255. Scale is a bit of misnomer
at this point, it slides the values up or down and then clips values still outside of the range.

 -- Christopher Stoll, UAkron, 2014
"""

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
	
	# recompose the trimmed SVD matrices back into matrix A
	A = numpy.dot(numpy.dot(matrixU, numpy.diag(matrixScopy)), matrixVt)

	# attempt the handle out of range values (TODO: pull out to own function)
	if rescale:
		curMin = 0
		curMax = 0
		# find min and max values
		for n in numpy.nditer(A):
			if int(round(n)) < curMin:
				curMin = int(round(n))
			if int(round(n)) > curMax:
				curMax = int(round(n))
		# shift values up
		if curMax < depth and curMin < 0:
			shiftVal = depth - curMax
			for t in numpy.nditer(A, op_flags=["readwrite"]):
				t[...] = t + shiftVal
				if t > depth:
					t[...] = depth
				elif t < 0:
					t[...] = 0
		# shift values down
		elif curMax > depth and curMin > 0:
			shiftVal = curMin
			for t in numpy.nditer(A, op_flags=["readwrite"]):
				t[...] = t - shiftVal
				if t > depth:
					t[...] = depth
				elif t < 0:
					t[...] = 0
		# no chance to shift, just chop (TODO: perform some sort of scaling)
		else:
			for t in numpy.nditer(A, op_flags=["readwrite"]):
				if t > depth:
					t[...] = depth
				elif t < 0:
					t[...] = 0

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
		pixelr, pixelg, pixelb = pixel
		image.matrix[row][col] = int(pixelr)
		col += 1
	
	return image
	

def process_svd(source_file, destination_file, kmin, kmax, rescale, contrast):
	"""
	Read from file provided on the command line or from stdin
	then save uncompressed representations of the SVD compressed version
	"""
	image = read_matrix_from_file(source_file)

	M = numpy.asmatrix(image.matrix)
	U, s, Vt = numpy.linalg.svd(M, full_matrices=True)
	
	write_matrices_to_file(U, s, Vt, kmin, kmax, image.width, image.height, image.depth, destination_file, rescale, contrast)



if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("infile", help="The source PNG file", type=argparse.FileType('r'), metavar='file')
	parser.add_argument("outfile", help="The destination PNG file", type=argparse.FileType('w'))
	parser.add_argument("-j", "--kmin", help="The number of high k values to exlude", type=int, default=0)
	parser.add_argument("-k", "--kmax", help="The number k values to use", type=int, default=0)
	parser.add_argument("-s", "--scale", help="Fit resulting image depth into '0 < n < depth' bounds", action="store_true")
	parser.add_argument("-c", "--contrast", help="Improve high contrast images", action="store_true")
	args = parser.parse_args()

	try:
		process_svd(args.infile.name, args.outfile.name, args.kmin, args.kmax, args.scale, args.contrast)
	except KeyboardInterrupt:
		exit(0)
