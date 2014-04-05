#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import argparse
import math
from PIL import Image


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
	filenames = []
	eigen_images = []
	dirname = source_directory[0]
	if os.path.isdir(dirname):
		for filename in os.listdir(dirname):
			if os.path.exists(os.path.join(dirname, filename)):
				image_as_vector = add_to_matrix_from_file(os.path.join(dirname, filename))
				eigen_images.append(image_as_vector[:])
				filenames.append(filename)
	else:
		for filename in source_directory:
			if os.path.exists(filename):
				image_as_vector = add_to_matrix_from_file(filename)
				eigen_images.append(image_as_vector[:])
				filenames.append(filename)
	return filenames, eigen_images


def cosine_similarity(img_a, img_b):
	numerator = 0
	denominatorA = 0
	denominatorB = 0
	for index, feature in enumerate(img_a):
		numerator += img_b[index] * img_a[index]
		denominatorA += img_b[index] * img_b[index]
		denominatorB += img_a[index] * img_a[index]
	
	if denominatorA and denominatorB:
		total_score = numerator / (math.sqrt(denominatorA) * math.sqrt(denominatorB))
	else:
		total_score = 0

	return int(round(total_score * 100))


def group_eigen_images(eigen_images, eigen_files):
	width = len(eigen_images)
	scores = [[0 for j in xrange(width)] for i in xrange(width)]

	print ',',
	for col_index, col_image in enumerate(eigen_images):
		print eigen_files[col_index].split('_')[0] + ',',
	print

	for col_index, col_image in enumerate(eigen_images):
		print eigen_files[col_index].split('_')[0] + ',',
		for row_index, row_image in enumerate(eigen_images):
			scores[col_index][row_index] = cosine_similarity(col_image, row_image)
			print str(scores[col_index][row_index]) + ',',
		print


def add_to_bin(bins, item_a, item_b):
	bin_count = len(bins)
	bin_found = False

	for x in xrange(0, bin_count):
		if bin_found:
			break

		for y in xrange(0, bin_count):
			if bins[x][y] == -1:
				if bin_found:
					bins[x][y] = unbined
				else:
					if y == 0:
						bins[x][y] = item_a
						bins[x][y+1] = item_b
						bin_found = True
				break

			if bins[x][y] == item_a or bins[x][y] == item_b:
				bin_found = True
				if bins[x][y] == item_a:
					unbined = item_b
				elif bins[x][y] == item_b:
					unbined = item_a
	return bins


def show_eigen_groups(eigen_images, eigen_files):
	width = len(eigen_images)
	scores = [[0 for j in xrange(width)] for i in xrange(width)]

	for col_index, col_image in enumerate(eigen_images):
		for row_index, row_image in enumerate(eigen_images):
			scores[col_index][row_index] = cosine_similarity(col_image, row_image)

	bins = [[-1 for j in xrange(width)] for i in xrange(width)]

	for x in xrange(0, width):
		esum = 0
		#print eigen_files[x].split('_')[0],
		for y in xrange(0, width):
			esum += scores[x][y]
			if scores[x][y] > 99:
				pass
			elif scores[x][y] > 80:
				add_to_bin(bins, eigen_files[x].split('_')[0], eigen_files[y].split('_')[0])
				#print eigen_files[y].split('_')[0], #scores[x][y],
		print eigen_files[x].split('_')[0], esum

	# bin_count = len(bins)
	# print
	# for x in xrange(0, bin_count):
	# 	if bins[x][0] == -1:
	# 		break

	# 	for y in xrange(0, bin_count):
	# 		if bins[x][y] == -1:
	# 			break
	# 		else:
	# 			print bins[x][y],
	# 	print
	# 	print


def create_eigenimage(source_directory):
	eigen_files, eigen_images = read_images(source_directory)
	#group_eigen_images(eigen_images, eigen_files)
	show_eigen_groups(eigen_images, eigen_files)


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	#parser.add_argument("file", help="The desintation file", type=argparse.FileType('w'))
	parser.add_argument('sourcedirectory', help="Where to store the image files", nargs='+')
	args = parser.parse_args()

	try:
		create_eigenimage(args.sourcedirectory)
	except KeyboardInterrupt:
		exit(0)
