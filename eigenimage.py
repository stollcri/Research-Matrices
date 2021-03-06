#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import argparse
import math
import numpy
import pickle
from PIL import Image

DEBUG_PRINT_EIGENIMAGES = False
DEBUG_TEST_EIGENSPACE = False

"""
	./eigenimage.py ./img/train-png/*-[123]*.png
"""

def get_k_limit(sigma):
	klimit = 0
	last_eigenvalue = 0
	eigenvalues = numpy.nditer(sigma, flags=['f_index'])
	while not eigenvalues.finished:
		if eigenvalues.index > 4:
			if last_eigenvalue:
				if (eigenvalues[0] * 10) < last_eigenvalue:
					klimit = eigenvalues.index - 1
					break
		last_eigenvalue = eigenvalues[0]
		klimit += 1
		eigenvalues.iternext()
	if klimit > 1024:
		return 1024
	else:
		return klimit


def add_to_matrix_from_file(filename):
	"""
	Read a PNG file and create an Image object from it
	"""
	if not os.path.exists(filename):
		return []

	png_image = Image.open(filename)
	#
	# EXPERIMENTS: how does changing the thumbnail size impact OCR
	# ~~~~~ MUST BE HARMONIZED WITH ocr-eig.py ~~~~~
	#
	image_size_final = 16
	png_image.thumbnail((image_size_final, image_size_final), Image.ANTIALIAS)

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

	return eigen_images, eigen_means


def create_eigenspace(eigen_images):
	A = numpy.asmatrix(eigen_images)
	At = A.transpose()
	
	# covariance matrix
	C = A * At

	# get eigen vectors
	U, s, Vt = numpy.linalg.svd(C, full_matrices=True)

	# project faces onto eigenvectors
	imagespace=numpy.dot(At, U)
	imagespace=imagespace.transpose()

	# TODO: FIXUP this area
	# normalize the imagespace
	img_width = int(math.sqrt(len(eigen_images[0])))
	for i in range(len(eigen_images)):
		ui=imagespace[i]
		ui.shape=(img_width,img_width)
		norm=numpy.trace(numpy.dot(ui.transpose(), ui))            
		imagespace[i]=imagespace[i]/norm 

	klimit = get_k_limit(s)
	imagespace = imagespace[:klimit]
	# s_len = s.shape[0]
	# for k in xrange(0, s_len):
	# 	if k >= klimit:
	# 		s[k] = 0
	s = s[:klimit]

	return imagespace, klimit, s


def write_eigenimages_individual(imagespace, klimit, filename):
	for z in xrange(0, klimit):
		row = imagespace[z]
		height, width = row.shape
		eigenimage = [0 for i in xrange(width)]
		col_max = -999999
		col_min = 999999
		for i in range(width):
			col = row[0, i]
			eigenimage[i] = col
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
		write_image_to_file(eigenimage, filename+"_k-"+str(z)+".png")


def write_eigenimage(imagespace, klimit, filename_postfix='0'):
	row = imagespace[0]
	height, width = row.shape
	eigenimage = [0 for i in xrange(width)]

	# layer on the eigen vectors
	for z in xrange(0, klimit):
		row = imagespace[z]
		for i in range(width):
			col = row[0, i]
			eigenimage[i] += col

	# scale the image depth
	col_max = -999999
	col_min = 999999
	for i in xrange(0, width):
		col = eigenimage[i]
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

	write_image_to_file(eigenimage, "./out/_EIMGS_"+filename_postfix+".png")


def generate_weights(imagespace, klimit, eigen_means):
	character_list = [ "./img/means/001_n.png", "./img/means/002_n.png", "./img/means/003_n.png", "./img/means/004_n.png", "./img/means/005_n.png", "./img/means/006_n.png", "./img/means/007_n.png", "./img/means/008_n.png", "./img/means/009_n.png", "./img/means/010_n.png", "./img/means/011_n.png", "./img/means/012_n.png", "./img/means/013_n.png", "./img/means/014_n.png", "./img/means/015_n.png", "./img/means/016_n.png", "./img/means/0_n.png", "./img/means/1_n.png", "./img/means/2_n.png", "./img/means/3_n.png", "./img/means/4_n.png", "./img/means/5_n.png", "./img/means/6_n.png", "./img/means/7_n.png", "./img/means/8_n.png", "./img/means/9_n.png", "./img/means/A_u.png", "./img/means/B_u.png", "./img/means/C_u.png", "./img/means/D_u.png", "./img/means/E_u.png", "./img/means/F_u.png", "./img/means/G_u.png", "./img/means/H_u.png", "./img/means/I_u.png", "./img/means/J_u.png", "./img/means/K_u.png", "./img/means/L_u.png", "./img/means/M_u.png", "./img/means/N_u.png", "./img/means/O_u.png", "./img/means/P_u.png", "./img/means/Q_u.png", "./img/means/R_u.png", "./img/means/S_u.png", "./img/means/T_u.png", "./img/means/U_u.png", "./img/means/V_u.png", "./img/means/W_u.png", "./img/means/X_u.png", "./img/means/Y_u.png", "./img/means/Z_u.png", "./img/means/a_l.png", "./img/means/b_l.png", "./img/means/c_l.png", "./img/means/d_l.png", "./img/means/e_l.png", "./img/means/f_l.png", "./img/means/g_l.png", "./img/means/h_l.png", "./img/means/i_l.png", "./img/means/j_l.png", "./img/means/k_l.png", "./img/means/l_l.png", "./img/means/m_l.png", "./img/means/n_l.png", "./img/means/o_l.png", "./img/means/p_l.png", "./img/means/q_l.png", "./img/means/r_l.png", "./img/means/s_l.png", "./img/means/t_l.png", "./img/means/u_l.png", "./img/means/v_l.png", "./img/means/w_l.png", "./img/means/x_l.png", "./img/means/y_l.png", "./img/means/z_l.png"]
	characters = []
	weights = []
	for character in character_list:
		image_name = os.path.splitext(os.path.basename(character))[0]
		letter, letter_case = image_name.split('_')
		if letter == '001':
			letter = '.'
		elif letter == '002':
			letter = ','
		elif letter == '003':
			letter = '?'
		elif letter == '004':
			letter = '!'
		elif letter == '005':
			letter = '-'
		elif letter == '006':
			letter = '_'
		elif letter == '007':
			letter = '#'
		elif letter == '008':
			letter = '@'
		elif letter == '009':
			letter = ';'
		elif letter == '010':
			letter = '\''
		elif letter == '011':
			letter = '"'
		elif letter == '012':
			letter = '('
		elif letter == '013':
			letter = ')'
		elif letter == '014':
			letter = '$'
		elif letter == '015':
			letter = '%'
		elif letter == '016':
			letter = '/'
		characters.append(letter)

		new_weight = generate_weight(imagespace, klimit, character, eigen_means)
		weights.append(new_weight)
	return characters, weights


def generate_weight(imagespace, klimit, test_img_name, eigen_means):
	test_img = add_to_matrix_from_file(test_img_name)

	# # subtract the imagespace mean
	# for index, value in enumerate(test_img):
	# 	test_img[index] = test_img[index] - eigen_means[index]

	test_array = numpy.array(test_img)
	weights = []
	for x in xrange(0, klimit):
		eigen_vector = imagespace[x].transpose()
		weights.append(numpy.dot(test_array, eigen_vector)[0,0])
	return weights


def test_one_go(imagespace, klimit, test_img_name, eigen_values, filename_postfix='0'):
	test_img = add_to_matrix_from_file(test_img_name)
	test_array = numpy.array(test_img)
	weights = []
	# get the weights for the unseeen image by projecting it down to eigenimagespace
	for x in xrange(0, klimit):
		eigen_vector = imagespace[x].transpose()
		weights.append(numpy.dot(test_array, eigen_vector)[0,0])

	# regenerate the unseen from weights, eigen values and imagespace
	row = 0
	col = 0
	height, width = imagespace.shape
	new_imagespace = imagespace.copy()
	for x in numpy.nditer(new_imagespace, op_flags=['readwrite']):
		x[...] = ((x * weights[row]) * eigen_values[row]) #+ means[col]
		col += 1
		if col >= width:
			row += 1
			col = 0
	write_eigenimage(new_imagespace, klimit, filename_postfix)


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
		png_image.putpixel((col, row), int(pixel))
		col += 1

	png_image.save(target_file)


def create_eigenimage(source_directory):
	"""
	Read from file provided on the command line or from stdin
	then save uncompressed representations of the SVD compressed version
	"""
	eigenspace_pickle = "./out/eigenspace.p"
	if os.path.exists(eigenspace_pickle):
		print "Loading values from cache", eigenspace_pickle
		eigenspace = pickle.load(open(eigenspace_pickle, "rb"))
		k_limit = eigenspace["k_limit"]
		image_space = eigenspace["image_space"]
		eigen_means = eigenspace["eigen_means"]
		eigen_values = eigenspace["eigen_values"]
		print " image_space", image_space.shape
		print " k_limit", k_limit
		print " eigen_values", eigen_values.shape
	else:
		print "No cache, generating eigenimagespace"
		eigen_images = read_images(source_directory)
		print " rows", len(eigen_images), "cols", len(eigen_images[0])

		eigen_images_mean, eigen_means = center_eigen(eigen_images)
		print " images", len(eigen_images_mean), "means", len(eigen_means)
		
		image_space, k_limit, eigen_values = create_eigenspace(eigen_images_mean)
		print " image_space", image_space.shape
		print " k_limit", k_limit
		print " eigen_values", eigen_values.shape
		eigenspace = {}
		eigenspace["k_limit"] = k_limit
		eigenspace["image_space"] = image_space
		eigenspace["eigen_means"] = eigen_means
		eigenspace["eigen_values"] = eigen_values
		pickle.dump(eigenspace, open(eigenspace_pickle, "wb"))

	charweight_pickle = "./out/characters.p"
	if os.path.exists(charweight_pickle):
		print "Loading values from cache", charweight_pickle
		character_weights = pickle.load(open(charweight_pickle, "rb"))
		characters = character_weights["characters"]
		weights = character_weights["weights"]
	else:
		print "No cache, generating all character weights"
		characters, weights = generate_weights(image_space, k_limit, eigen_means)
		character_weights = {}
		character_weights["characters"] = characters
		character_weights["weights"] = weights
		pickle.dump(character_weights, open(charweight_pickle, "wb"))

	if DEBUG_PRINT_EIGENIMAGES:
		write_eigenimages_individual(image_space, k_limit, "./out/_EIMG")
		write_eigenimage(image_space, 4, "04")
		write_eigenimage(image_space, 8, "08")
		write_eigenimage(image_space, 16, "16")
		write_eigenimage(image_space, 32, "32")

	if DEBUG_TEST_EIGENSPACE:
		print "Generating check images"
		# test the imagespace's ability to reproduce characters
		test_one_go(image_space, k_limit, "./img/means/003_n.png", eigen_values, filename_postfix="01")
		test_one_go(image_space, k_limit, "./img/means/008_n.png", eigen_values, filename_postfix="02")
		test_one_go(image_space, k_limit, "./img/means/g_l.png", eigen_values, filename_postfix="03")
		test_one_go(image_space, k_limit, "./img/means/H_u.png", eigen_values, filename_postfix="04")
		test_one_go(image_space, k_limit, "./img/means/Q_u.png", eigen_values, filename_postfix="05")


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('sourcedirectory', help="Where to store the image files", nargs='+')
	args = parser.parse_args()

	try:
		create_eigenimage(args.sourcedirectory)
	except KeyboardInterrupt:
		exit(0)
