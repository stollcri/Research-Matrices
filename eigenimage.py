#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import argparse
import math
import numpy
from PIL import Image

"""
	./eigenimage.py ./img/train-png/*-[123]*.png
"""

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
	write_image_to_file(eigen_means, "./out/_TEST_AVG.png")

	# Get the difference from the mean (Φ) = Φ=Γ−Ψ
	for i in xrange(image_count):
		for j in xrange(image_size):
			eigen_images[i][j] = eigen_images[i][j] - eigen_means[j]

	return eigen_images, eigen_means


def create_eigenspace(eigen_images):
	A = numpy.asmatrix(eigen_images)
	At = A.transpose()
	
	# covariance matrix
	C = A * At
	print "A", A.shape
	print "At", At.shape
	print "C", C.shape

	# get eigen vectors
	U, s, Vt = numpy.linalg.svd(C, full_matrices=True)

	print "U", U.shape
	# project faces onto eigenvectors
	imagespace=numpy.dot(At,U)
	imagespace=imagespace.transpose()
	print "imagespace", imagespace.shape

	# TODO: FIXUP this area
	img_width = int(math.sqrt(len(eigen_images[0])))
	for i in range(len(eigen_images)):
		ui=imagespace[i]
		ui.shape=(img_width,img_width)
		norm=numpy.trace(numpy.dot(ui.transpose(), ui))            
		imagespace[i]=imagespace[i]/norm 

	# klimit = min(256, get_k_limit(s))
	klimit = get_k_limit(s)
	print "klimit", klimit
	# i = 0
	# for t in numpy.nditer(s, op_flags=["readwrite"]):
	# 	if i > klimit:
	# 		t[...] = 0
	# 	i += 1
	# S = numpy.diag(s)
	# musm, musn = U.shape
	# mvsm, mvsn = Vt.shape
	# if musn != mvsm:
	# 	zeros = numpy.zeros((musn, mvsm), dtype=numpy.int32)
	# 	zeros[:S.shape[0], :S.shape[1]] = S
	# 	S = zeros

	# scores = U*S
	imagespace = imagespace[:klimit]
	print "imagespace", imagespace.shape
	return imagespace, klimit, s


def write_eigenimages(imagespace, klimit, filename_postfix='0'):
	# each individual eigen face
	# write_eigenimages_all(imagespace, klimit, filename_postfix)
	# all the eigenfaces together
	write_eigenimages_one(imagespace, klimit, filename_postfix)

def write_eigenimages_all(imagespace, klimit, filename_postfix='0'):
	for z in xrange(0, klimit):
		row = imagespace[z]
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
		write_image_to_file(eigenimage, "./out/_TEST_"+filename_postfix+".png")

	return numpy.asarray(imagespace).reshape(-1)


def write_eigenimages_one(imagespace, klimit, filename_postfix='0'):
	row = imagespace[0]
	height, width = row.shape
	eigenimage = [0 for i in xrange(width)]

	for z in xrange(0, klimit):
		row = imagespace[z]
		for i in range(width):
			col = row[0, i]
			eigenimage[i] += col

	col_max = -999999
	col_min = 999999
	for i in xrange(0, width):
		col = eigenimage[i]
		# print eigenimage[i]
		if col < col_min:
			col_min = col
		if col > col_max:
			col_max = col

	col_shift = col_min * -1
	col_range = col_max - col_min
	col_scale = 255 / col_range
	# print col_shift, col_range, col_scale
	# print col_min, col_min+col_shift, int(round((col_min+col_shift) * col_scale))
	# print col_max, col_max+col_shift, int(round((col_max+col_shift) * col_scale))
	for i in xrange(0, width):
		eigenimage[i] += col_shift
		eigenimage[i] = int(round(eigenimage[i] * col_scale))
	write_image_to_file(eigenimage, "./out/_TEST_"+filename_postfix+".png")

	# print numpy.asarray(imagespace).reshape(-1)
	return numpy.asarray(imagespace).reshape(-1)


def test_one(means, imagespace, klimit, eigen_values):
	test_img_name = "./img/train-png/0_n-93.png"
	test_one_go(means, imagespace, klimit, test_img_name, eigen_values, "0-93")

	test_img_name = "./img/train-png/0_n-102.png"
	test_one_go(means, imagespace, klimit, test_img_name, eigen_values, "0-102")

	test_img_name = "./img/train-png/3_n-121.png"
	test_one_go(means, imagespace, klimit, test_img_name, eigen_values, "3-121")

	test_img_name = "./img/train-png/A_u-122.png"
	test_one_go(means, imagespace, klimit, test_img_name, eigen_values, "A-122")

	test_img_name = "./img/train-png/C_u-58.png"
	test_one_go(means, imagespace, klimit, test_img_name, eigen_values, "C-58")

	test_img_name = "./img/train-png/D_u-103.png"
	test_one_go(means, imagespace, klimit, test_img_name, eigen_values, "D-103")

	test_img_name = "./img/train-png/E_u-28.png"
	test_one_go(means, imagespace, klimit, test_img_name, eigen_values, "E-28")

	test_img_name = "./img/train-png/m_l-77.png"
	test_one_go(means, imagespace, klimit, test_img_name, eigen_values, "m-77")

	test_img_name = "./img/train-png/O_u-9.png"
	test_one_go(means, imagespace, klimit, test_img_name, eigen_values, "O-9")

	test_img_name = "./img/train-png/Q_u-6.png"
	test_one_go(means, imagespace, klimit, test_img_name, eigen_values, "q-6")

	test_img_name = "./img/train-png/s_l-9.png"
	test_one_go(means, imagespace, klimit, test_img_name, eigen_values, "s-9")


def test_one_go(means, imagespace, klimit, test_img_name, eigen_values, filename_postfix='0'):
	test_img = add_to_matrix_from_file(test_img_name)
	test_array = numpy.array(test_img)
	weights = []
	for x in xrange(0, klimit):
		eigen_vector = imagespace[x].transpose()
		# print "test_array", test_array.shape, test_array
		# print "eigen_vector", eigen_vector.shape, eigen_vector
		# print "dot", numpy.dot(test_array, eigen_vector)[0,0]
		weights.append(numpy.dot(test_array, eigen_vector)[0,0])

	row = 0
	col = 0
	height, width = imagespace.shape
	imagespace = imagespace.copy()
	for x in numpy.nditer(imagespace, op_flags=['readwrite']):
		# print row, "/", col, ":", x, weights[row], means[col], ((x * weights[row]) + means[col])
		x[...] = ((x * weights[row]) * eigen_values[row]) #+ means[col]
		col += 1
		if col >= width:
			row += 1
			col = 0

	# print imagespace
	# print weights[0], weights[1]
	# print imagespace
	write_eigenimages(imagespace, klimit, filename_postfix)


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


def create_eigenimage(source_directory):
	"""
	Read from file provided on the command line or from stdin
	then save uncompressed representations of the SVD compressed version
	"""
	eigen_images = read_images(source_directory)
	eigen_images_mean, eigen_means = center_eigen(eigen_images)
	face_space, k_limit, eigen_values = create_eigenspace(eigen_images_mean)
	# write_eigenimages(face_space, k_limit)
	test_one(eigen_means, face_space, k_limit, eigen_values)


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
	parser.add_argument('sourcedirectory', help="Where to store the image files", nargs='+')
	args = parser.parse_args()

	try:
		create_eigenimage(args.sourcedirectory)
	except KeyboardInterrupt:
		exit(0)
