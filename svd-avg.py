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
		self.matrix = [[0 for j in xrange(width)] for i in xrange(height)]


def get_k_limit(sigma, sigma_width):
	klimit = 8
	last_eigenvalue = 0
	eigenvalues = numpy.nditer(sigma, flags=['f_index'])
	while not eigenvalues.finished:
		if eigenvalues.index > 4:
			if last_eigenvalue:
				if (eigenvalues[0] * 10) < last_eigenvalue:
					klimit = eigenvalues.index - 1
					break
		last_eigenvalue = eigenvalues[0]
		eigenvalues.iternext()

	if klimit > sigma_width:
		klimit = int(sigma_width / 2)

	return klimit


def merge_matrices(imagea, imageb, kmax, contrast=False):
	# decompose the image matrices
	Ma = numpy.asmatrix(imagea.matrix)
	Mb = numpy.asmatrix(imageb.matrix)
	Ua, sa, Vta = numpy.linalg.svd(Ma, full_matrices=True)
	Ub, sb, Vtb = numpy.linalg.svd(Mb, full_matrices=True)

	# Use the provided k max as the klimit,
	# check for a large drop in eigenvalues
	if kmax > 0:
		klimit = kmax
	else:
		klimita = get_k_limit(sa, (imagea.width / 2))
		klimitb = get_k_limit(sb, (imagea.width / 2))
		klimit = max(klimita, klimitb)

	# copy in columns from both U matrices
	tmpUm, tmpUn = Ua.shape
	tempU = numpy.zeros((tmpUm, tmpUm), dtype=numpy.float)
	for k in xrange(0, klimit):
		for j in xrange(0, imagea.width):
			tempU[j, (k*2)] = Ua[j, k]
	
		for j in xrange(0, imagea.width):
			tempU[j, ((k*2)+1)] = Ub[j, k]

	# copy in rows from both Vt matrices
	tmpVtm, tmpVtn = Vta.shape
	tempVt = numpy.zeros((tmpVtm, tmpVtm), dtype=numpy.float)
	for k in xrange(0, klimit):
		for j in xrange(0, imagea.height):
			tempVt[(k*2), j] = Vta[k, j]
	
		for j in xrange(0, imagea.height):
			tempVt[((k*2)+1), j] = Vtb[k, j]

	# copy in rows from both s arrays
	tmpSam = sa.shape[0]
	matrixScopy = sa.copy()
	for k in xrange(0, tmpSam):
		if k >= ((2 * klimit) + 1):
			matrixScopy[k] = 0
		else:
			if k % 2:
				#matrixScopy[k] = sb[int(k/2)] *.25
				matrixScopy[k] = sb[int(k/2)] *.3
			else:
				#matrixScopy[k] = sa[int(k/2)] *.75
				matrixScopy[k] = sa[int(k/2)] *.7

	# shape the eigenvalue matrix to fit both U and Vt
	# e.g.: m_U_m * m_S_n * n_Vt_n
	matrixScopy = numpy.diag(matrixScopy)
	musm, musn = tempU.shape
	mvsm, mvsn = tempVt.shape
	if musn != mvsm:
		zeros = numpy.zeros((musn, mvsm), dtype=numpy.float)
		zeros[:matrixScopy.shape[0], :matrixScopy.shape[1]] = matrixScopy
		matrixScopy = zeros

	# recompose the matrices into one
	matrixComposed = numpy.dot(numpy.dot(tempU, matrixScopy), tempVt)

	if contrast:
		depth = imagea.depth
		depth_min = int(depth - (depth * .75))
		depth_max = int(depth - (depth * .25))
		for t in numpy.nditer(matrixComposed, op_flags=["readwrite"]):
			if t < depth_min:
				t[...] = 0
			elif t > depth_max:
				t[...] = depth
			else:
				t[...] = t - (t / 7)
	return matrixComposed


def write_matrices_to_file(imagea, imageb, kmax, filename, contrast=False):
	A = merge_matrices(imagea, imageb, kmax, contrast)
	width = imagea.width
	height = imagea.height

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
	png_image.thumbnail((32, 32), Image.ANTIALIAS)

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

	return image
	

def process_svd(source_file_a, source_file_b, destination_file, kmax, contrast):
	"""
	Read from file provided on the command line or from stdin
	then save uncompressed representations of the SVD compressed version
	"""
	imagea = read_matrix_from_file(source_file_a)
	imageb = read_matrix_from_file(source_file_b)
	write_matrices_to_file(imagea, imageb, kmax, destination_file, contrast)



if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("infile1", nargs='?', help="The source ASCII PGM file", type=argparse.FileType('r'), default=sys.stdin)
	parser.add_argument("infile2", nargs='?', help="The source ASCII PGM file", type=argparse.FileType('r'), default=sys.stdin)
	parser.add_argument("outfile", nargs='?', help="The destination ASCII PGM file", type=argparse.FileType('w'), default=sys.stdout)
	parser.add_argument("-k", "--kmax", help="The number k values to use", type=int, default=0)
	parser.add_argument("-c", "--contrast", help="Improve high contrast images", action="store_true")
	args = parser.parse_args()

	try:
		process_svd(args.infile1, args.infile2, args.outfile, args.kmax, args.contrast)
	except KeyboardInterrupt:
		exit(0)
