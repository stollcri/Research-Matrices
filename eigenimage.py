#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import argparse
import math
import numpy
from PIL import Image


def get_k_limit(sigma):
	klimit = 0
	last_eigenvalue = 0
	eigenvalues = numpy.nditer(sigma, flags=['f_index'])
	while not eigenvalues.finished:
		klimit += 1
		if eigenvalues.index > 4:
			if last_eigenvalue:
				if (eigenvalues[0] * 10) < last_eigenvalue:
					klimit = eigenvalues.index - 1
					break
		# print last_eigenvalue, eigenvalues[0]
		last_eigenvalue = eigenvalues[0]
		eigenvalues.iternext()

	return klimit


def add_to_matrix_from_file(filename):
	"""
	Read a PNG file and create an Image object from it
	"""
	if not os.path.exists(filename):
		return []

	png_image = Image.open(filename)
	png_image.thumbnail((32, 32), Image.ANTIALIAS)

	col = 0
	image = []
	for pixel in list(png_image.getdata()):
		# TODO: something better than taking the red value
		if png_image.mode == 'L':
			pixelr = pixel
		elif png_image.mode == 'RGB':
			pixelr, pixelg, pixelb = pixel
		elif png_image.mode == 'RGBA':
			pixelr, pixelg, pixelb, pixela = pixel
		image.append(int(pixelr))
		col += 1
	return image


def read_images(source_directory):
	eigen_images = []
	dirname = source_directory[0]
	if os.path.isdir(dirname):
		for filename in os.listdir(dirname):
			if filename[0] != '.':
				if os.path.exists(os.path.join(dirname, filename)):
					image_as_vector = add_to_matrix_from_file(os.path.join(dirname, filename))
					eigen_images.append(image_as_vector[:])
	else:
		for filename in source_directory:
			if os.path.exists(filename):
				image_as_vector = add_to_matrix_from_file(filename)
				eigen_images.append(image_as_vector[:])
	return eigen_images


def center_eigen(eigen_images):
	image_count = len(eigen_images)
	image_size = len(eigen_images[0])

	# Aready have (Φ), eigen_images
	eigen_means = [0 for i in xrange(image_size)]

	# Get the mean image (Ψ), step 1 sum
	for image in eigen_images:
		for index, pixel in enumerate(image):
			# TODO: overflow prevention?
			eigen_means[index] += pixel
	
	# Get the mean image (Ψ), step 2 divide
	for i in xrange(len(eigen_means)):
		eigen_means[i] = eigen_means[i] / image_count

	# Get the difference from the mean (Φ) = Φ=Γ−Ψ
	for i in xrange(image_count):
		for j in xrange(image_size):
			eigen_images[i][j] = eigen_images[i][j] - eigen_means[j]

	A = numpy.asmatrix(eigen_images)
	# At = A.transpose()
	# L = A * At
	# s, u = numpy.linalg.eig(L)
	U, s, Vt = numpy.linalg.svd(A, full_matrices=True)

	klimit = min(16, get_k_limit(s))
	print "A.shape", A.shape
	print "A.shape[0]", A.shape[0]
	print "s.shape", s.shape
	print "klimit", klimit
	i = 0
	for t in numpy.nditer(s, op_flags=["readwrite"]):
		if i > klimit:
			t[...] = 0
		i += 1
	S = numpy.diag(s)
	musm, musn = U.shape
	mvsm, mvsn = Vt.shape
	if musn != mvsm:
		zeros = numpy.zeros((musn, mvsm), dtype=numpy.int32)
		zeros[:S.shape[0], :S.shape[1]] = S
		S = zeros

	scores = U*S
	facespace = Vt[:klimit]
	print facespace.shape

	for z in xrange(0, klimit):
		row = facespace[z]
		height, width = row.shape
		eigenimage = [0 for i in xrange(width)]
		col_max = -999999
		col_min = 999999
		for i in range(width):
			col = row[0, i]
			eigenimage[i] = col
			# print eigenimage[i]
			if col < col_min:
				col_min = col
			if col > col_max:
				col_max = col

		col_shift = col_min * -1
		col_range = col_max - col_min
		col_scale = 255 / col_range
		for i in xrange(0, width):
			eigenimage[i] += col_shift
			eigenimage[i] = int(round(eigenimage[i] * col_scale))
		#write_image_to_file(eigenimage, "./out/_TEST_"+str(z)+".png")

	# print numpy.asarray(facespace).reshape(-1)
	return numpy.asarray(facespace).reshape(-1)



	# I = numpy.dot(numpy.dot(U, S), Vt)
	I = numpy.dot(A, Vt)
	print I

	# print s
	# print U
	print "U.shape", U.shape
	# print "S.shape", S.shape
	print "Vt.shape", Vt.shape
	print "I.shape", I.shape

	height, width = A.shape
	eigenimage = [0 for i in xrange(width)]
	col_max = 0
	col_min = 999999
	n = 0
	for row in I:
		for i in range(row.shape[-1]):
			col = row[...,i][0, 0]
			eigenimage[i] = col
			# print col, eigenimage[i], 
			if col < col_min:
				col_min = col
			if col > col_max:
				col_max = col

		col_shift = col_min * -1
		col_range = col_max - col_min
		col_scale = 255 / col_range
		for i in xrange(0, width):
			eigenimage[i] += col_shift
			eigenimage[i] = int(round(eigenimage[i] * col_scale))
		write_image_to_file(eigenimage, "./out/_TEST_"+str(n)+".png")
		n += 1

		break

	# col_shift = col_min * -1
	# col_range = col_max - col_min
	# col_scale = 255 / col_range
	# print col_min, col_max, col_shift, col_range, col_scale
	# print (col_min + col_shift), round((col_min + col_shift) * col_scale)
	# print (col_max + col_shift), round((col_max + col_shift) * col_scale)

	# for i in xrange(0, width):
	# 	eigenimage[i] += col_shift
	# 	eigenimage[i] = int(round(eigenimage[i] * col_scale))
	# 	pass
	# print

	# return eigenimage
	return eigen_means


def write_image_to_file(eigen_image, target_file):
	width = int(math.sqrt(len(eigen_image)))
	png_image = Image.new('L', (width, width))
	
	row = 0
	col = 0
	for pixel in eigen_image:
		if col >= width:
			row += 1
			col = 0
		if row >= width:
			break
		# pixelval = int(eigen_image[row][col])
		# png_image.putpixel((row, col), pixelval)
		png_image.putpixel((col, row), int(pixel))
		col += 1

	png_image.save(target_file)


def create_eigenimage(source_directory, target_file):
	"""
	Read from file provided on the command line or from stdin
	then save uncompressed representations of the SVD compressed version
	"""
	eigen_images = read_images(source_directory)
	eigen_images_average = center_eigen(eigen_images)
	write_image_to_file(eigen_images_average, target_file)


"""
 TODO: make this work like eigenface (eigenimage) implementations
 		- Process a group of examples for each letter at once
 		- Read the images in (as is), but unwrap them as a row in the matrix
 		- Calculate the mean for each column and subtract it from each row
 		- Calculate the eigenvectors and eigenvalues of the covariance matrix
 (TODO should be done as a new file, this is a drastic change)
"""

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("eigenimage", help="The desintation PNG file", type=argparse.FileType('w'))
	parser.add_argument('sourcedirectory', help="Where to store the image files", nargs='+')
	args = parser.parse_args()

	try:
		create_eigenimage(args.sourcedirectory, args.eigenimage)
	except KeyboardInterrupt:
		exit(0)
