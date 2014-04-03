#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
# import sys
import argparse
# import numpy
import math
from PIL import Image


# def get_k_limit(sigma, sigma_width):
# 	klimit = 8
# 	last_eigenvalue = 0
# 	eigenvalues = numpy.nditer(sigma, flags=['f_index'])
# 	while not eigenvalues.finished:
# 		if eigenvalues.index > 4:
# 			if last_eigenvalue:
# 				if (eigenvalues[0] * 10) < last_eigenvalue:
# 					klimit = eigenvalues.index - 1
# 					break
# 		last_eigenvalue = eigenvalues[0]
# 		eigenvalues.iternext()

# 	if klimit > sigma_width:
# 		klimit = int(sigma_width / 2)

# 	return klimit


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

	# # Experiment with decomposing before averaging
	# row = 0
	# col = 0
	# image = [[]]
	# image = [[0 for j in xrange(32)] for i in xrange(32)]
	# for pixel in list(png_image.getdata()):
	# 	if col >= 32:
	# 		row += 1
	# 		col = 0
	# 	# TODO: something better than taking the red value
	# 	if png_image.mode == 'L':
	# 		pixelr = pixel
	# 	elif png_image.mode == 'RGB':
	# 		pixelr, pixelg, pixelb = pixel
	# 	elif png_image.mode == 'RGBA':
	# 		pixelr, pixelg, pixelb, pixela = pixel
	# 	image[row][col] = int(pixelr)
	# 	col += 1

	# # discard non principal components
	# M = numpy.asmatrix(image)
	# U, s, Vt = numpy.linalg.svd(M, full_matrices=True)
	# klimit = get_k_limit(s, 32)

	# for i in xrange(klimit,32):
	# 	s[i] = 0
	# # shape the eigenvalue matrix to fit both U and Vt
	# # e.g.: m_U_m * m_S_n * n_Vt_n
	# matrixScopy = numpy.diag(s)
	# musm, musn = U.shape
	# mvsm, mvsn = Vt.shape
	# if musn != mvsm:
	# 	zeros = numpy.zeros((musn, mvsm), dtype=numpy.float)
	# 	zeros[:matrixScopy.shape[0], :matrixScopy.shape[1]] = matrixScopy
	# 	matrixScopy = zeros

	# matrixComposed = numpy.dot(numpy.dot(U, matrixScopy), Vt)
	# image_fixed = numpy.asarray(matrixComposed).flatten()

	# return image_fixed


def read_images(source_directory):
	eigen_images = []
	dirname = source_directory[0]
	if os.path.isdir(dirname):
		for filename in os.listdir(dirname):
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

	eigen_means = [0 for i in xrange(image_size)]

	for image in eigen_images:
		for index, pixel in enumerate(image):
			eigen_means[index] += pixel
	
	for i in xrange(len(eigen_means)):
		eigen_means[i] = eigen_means[i] / image_count

	# for i in xrange(image_count):
	# 	for j in xrange(image_size):
	# 		eigen_images[i][j] = eigen_images[i][j] - eigen_means[j]

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
