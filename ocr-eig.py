#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import os
import math
import pickle
import numpy
import datetime
from PIL import Image, ImageDraw, ImageOps

DEBUG_LOCATIONS = False
DEBUG_VALUES = False
DEBUG_PRINT_CHARS = True
DEBUG_PRINT_EIGS = False

"""
To run:
	./ocr-eig.py ./img/RightsOfManB.png
	-- or --
	rm ./out/img* && ./ocr-eig.py ./img/RightsOfManB.png
"""

def show_time():
	return str(datetime.datetime.now())


def load_knowledge(eigenspace_pickle, charweight_pickle):
	if DEBUG_LOCATIONS: print show_time(), "> load_knowledge"
	if os.path.exists(eigenspace_pickle):
		eigenspace = pickle.load(open(eigenspace_pickle, "rb"))
		k_limit = eigenspace["k_limit"]
		image_space = eigenspace["image_space"]
		eigen_means = eigenspace["eigen_means"]
		eigen_values = eigenspace["eigen_values"]
	else:
		print "Eigenimagespace file", eigenspace_pickle, "not found."
		exit

	if os.path.exists(charweight_pickle):
		character_weights = pickle.load(open(charweight_pickle, "rb"))
		characters = character_weights["characters"]
		weights = character_weights["weights"]
	else:
		print "Character weights file", charweight_pickle, "not found."
		exit

	if DEBUG_LOCATIONS: print show_time(), "< load_knowledge"
	return k_limit, image_space, eigen_means, eigen_values, characters, weights


def read_and_split(filename):
	if DEBUG_LOCATIONS: print show_time(), "> read_and_split"
	if not os.path.exists(filename):
		return []

	png_image = Image.open(filename)
	png_width, png_height = png_image.size
	png_depth = 255
	png_array = [[0 for j in xrange(png_width)] for i in xrange(png_height)]

	row = 0
	col = 0
	for pixel in list(png_image.getdata()):
		if col >= png_width:
			row += 1
			col = 0
		if png_image.mode == 'L':
			pixelr = pixel
			png_pixel = pixelr
		elif png_image.mode == '1':
			pixelr = pixel
			png_pixel = pixelr
		elif png_image.mode == 'RGB':
			pixelr, pixelg, pixelb = pixel
			png_pixel = math.floor((pixelr + pixelg + pixelb) / 3)
		elif png_image.mode == 'RGBA':
			pixelr, pixelg, pixelb, pixela = pixel
			png_pixel = math.floor((pixelr + pixelg + pixelb) / 3)

		png_array[row][col] = int(png_pixel)
		col += 1
	if DEBUG_LOCATIONS: print show_time(), "< read_and_split"
	return find_characters(png_array, png_depth)


def find_characters(image_matrix, depth):
	if DEBUG_LOCATIONS: print show_time(), "> find_characters"
	threshhold = 128
	characters = []

	text_rows = []
	blank_row = True
	for row_index, row in enumerate(image_matrix):
		pixel_row = []

		for col in row:
			inv = depth - col
			if inv > threshhold:
				blank_row = False
			pixel_row.append(inv)

		if not blank_row:
			text_rows.append(pixel_row)
			blank_row = True
		else:
			if len(text_rows):
				results = split_characters(text_rows, threshhold, row_index)
				for result in results:
					characters.append(result)
				characters.append('\n')
				text_rows = []
	if DEBUG_LOCATIONS: print show_time(), "< find_characters"
	return characters


def split_characters(text_row, threshhold, row_index):
	row_count = len(text_row)
	column_count = len(text_row[0])
	space_width = 2 + int(round(column_count * .005))
	#print column_count, space_width
	characters = []

	text_cols = []
	blank_col = True
	space_cols = 0
	for col in xrange(0, column_count):
		pixel_col = []

		for row in xrange(0, row_count):
			if text_row[row][col] > threshhold:
				blank_col = False
			pixel_col.append(text_row[row][col])

		if not blank_col:
			if space_cols > 8:
				characters.append([''])
			elif space_cols > space_width:
				characters.append([' '])

			text_cols.append(pixel_col)
			blank_col = True
			space_cols = 0
			
		else:
			space_cols += 1
			if len(text_cols):
				filename = "./out/img_" + str(row_index) + "-" + str(col) + ".png"
				results = size_character(transpose_image(text_cols), filename)
				characters.append(results)
				text_cols = []

	return characters


def transpose_image(image_matrix):
	width = len(image_matrix[0])
	height = len(image_matrix)
	new_width = height
	new_height = width

	new_image_matrix = [[0 for j in xrange(new_width)] for i in xrange(new_height)]

	for row in xrange(0, width):
		for col in xrange(0, height):
			new_image_matrix[row][col] = image_matrix[col][row]

	return new_image_matrix


def size_character(eigen_image, target_file):
	width = len(eigen_image[0])
	height = len(eigen_image)
	tmp_image = Image.new('L', (width, height))
	
	row = 0
	col = 0
	for i in eigen_image:
		for j in i:
			if col >= width:
				row += 1
				col = 0
			tmp_image.putpixel((col, row), int(eigen_image[row][col]))
			col += 1
	
	# png_image = tmp_image.resize((32, 32))
	
	image_depth = 128
	x_left = find_crop_left(tmp_image, width, height, image_depth)
	x_right = find_crop_right(tmp_image, width, height, image_depth)
	y_top = find_crop_top(tmp_image, width, height, image_depth)
	y_bottom = find_crop_bottom(tmp_image, width, height, image_depth)
	one_image = tmp_image.crop((x_left, y_top, x_right, y_bottom))
	#png_image = new_image.resize((32, 32))
	#png_image = new_image.resize((16, 16))
	#png_image = new_image.resize((12, 12))

	fill_color = "#000000"
	image_size_work = 14
	image_size_final = 16

	width, height = one_image.size

	if width < 5 and height < 5:
		scale_w = image_size_work / float(max(width, height) * 1.4)
		scale_h = image_size_work / float(max(width, height) * 2.8)
	elif width < 4:
		scale_w = image_size_work / float(max(width, height) * 1.6)
		scale_h = image_size_work / float(max(width, height))
	elif width < 6:
		scale_w = image_size_work / float(max(width, height) * .8)
		scale_h = image_size_work / float(max(width, height))
	else:
		scale_w = image_size_work / float(max(width, height))
		scale_h = scale_w
	new_width = int(math.ceil(width * scale_w))
	new_height = int(math.ceil(height * scale_h))
	new_image = one_image.resize((new_width, new_height), Image.ANTIALIAS)

	# new_image = one_image

	new_image.thumbnail((image_size_final, image_size_final), Image.ANTIALIAS)
	png_image = Image.new('L', (image_size_final, image_size_final))
	new_draw = ImageDraw.Draw(png_image)
	new_draw.rectangle(((0, 0), (image_size_final, image_size_final)), fill_color)
	width, height = new_image.size
	originx = int(round((image_size_final - width) / 2))
	originy = int(round((image_size_final - height) / 2))
	png_image.paste(new_image, (originx, originy, originx+width, originy+height))

	#png_array = [0 for i in xrange(32 * 32)]
	#png_array = [0 for i in xrange(16 * 16)]
	png_array = [0 for i in xrange(image_size_final * image_size_final)]
	#
	# Uncomment to save out the captured characters
	#
	if DEBUG_PRINT_CHARS: png_image.save(target_file)
	for index, pixel in enumerate(png_image.getdata()):
		png_array[index] = int(pixel)

	return png_array


def find_crop_left(image, width, height, depth):
	found_fg_start = False
	for i in range(width):
		for j in range(height):
			if image.getpixel((i,j)) >= depth:
				found_fg_start = True
				return i
	return 0


def find_crop_right(image, width, height, depth):
	found_fg_start = False
	for i in range(width-1,0,-1):
		for j in range(height):
			if image.getpixel((i,j)) >= depth:
				found_fg_start = True
				return i+1
	return width


def find_crop_top(image, width, height, depth):
	found_fg_start = False
	for j in range(height):
		for i in range(width):
			if image.getpixel((i,j)) >= depth:
				found_fg_start = True
				return j
	return 0


def find_crop_bottom(image, width, height, depth):
	found_fg_start = False
	for j in range(height-1,0,-1):
		for i in range(width):
			if image.getpixel((i,j)) >= depth:
				found_fg_start = True
				return j+1
	return height




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
		#pixelval = int(eigen_image[row][col])
		#png_image.putpixel((row, col), pixelval)
		png_image.putpixel((col, row), int(pixel))
		col += 1

	png_image.save(target_file)

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
	
	write_image_to_file(eigenimage, "./out/_TEST_"+str(filename_postfix)+".png")

def write_question_image_projected(weights, imagespace, eigen_values, klimit, curchar):
	if DEBUG_LOCATIONS: print show_time(), "> write_question_image_projected"
	row = 0
	col = 0
	height, width = imagespace.shape
	new_imagespace = imagespace.copy()
	for x in numpy.nditer(new_imagespace, op_flags=['readwrite']):
		# print row, "/", col, ":", x, weights[row], means[col], ((x * weights[row]) + means[col])
		x[...] = ((x * weights[row]) * eigen_values[row]) #+ means[col]
		col += 1
		if col >= width:
			row += 1
			col = 0
	write_eigenimage(new_imagespace, klimit, curchar)
	if DEBUG_LOCATIONS: print show_time(), "< write_question_image_projected"

def test_knowledge(question, klimit, imagespace, eigen_means, eigen_values, characters, weights, curchar):
	if DEBUG_LOCATIONS: print show_time(), "> test_knowledge"

	# subtract the imagespace mean
	# for index, value in enumerate(question):
	# 	question[index] = question[index] - eigen_means[index]

	test_array = numpy.array(question)
	question_weights = []
	# get the weights for the unseeen image by projecting it down to eigenimagespace
	for x in xrange(0, klimit):
		eigen_vector = imagespace[x].transpose()
		# print "test_array", test_array.shape, test_array
		# print "eigen_vector", eigen_vector.shape, eigen_vector
		# print "dot", numpy.dot(test_array, eigen_vector)[0,0]
		question_weights.append(numpy.dot(test_array, eigen_vector)[0,0])

	#
	# DEBUG
	#
	if DEBUG_PRINT_EIGS: write_question_image_projected(question_weights, imagespace, eigen_values, klimit, curchar)

	# Cosine similarity
	scores = []
	for idx, weight_vector in enumerate(weights):
		doloop = True
		if lastchar.islower():
			if characters[idx].isupper():
				doloop = False

		if doloop:
			numerator = 0
			denominatorA = 0
			denominatorB = 0
			for index, feature in enumerate(weight_vector):
				numerator += question_weights[index] * weight_vector[index]
				denominatorA += question_weights[index] * question_weights[index]
				denominatorB += weight_vector[index] * weight_vector[index]
			if denominatorA and denominatorB:
				total_score = numerator / (math.sqrt(denominatorA) * math.sqrt(denominatorB))
			else:
				total_score = 0
		else:
			total_score = 0

		scores.append(total_score)

	max_score = -999999
	max_score_spot = -1
	for index, score in enumerate(scores):
		if DEBUG_VALUES: print characters[index], score, '\t', max_score
		if score > max_score:
			max_score = score
			max_score_spot = index
	if DEBUG_VALUES: print characters[max_score_spot], max_score

	answer = characters[max_score_spot]
	if DEBUG_LOCATIONS: print show_time(), "< test_knowledge"
	return answer, max_score


def start_ocr(text_image, k_limit, image_space, eigen_means, eigen_values, characters, weights):
	if not os.path.exists(text_image):
		return 0

	letters = read_and_split(text_image)
	result = ""
	i = 0
	for letter in letters:
		if len(letter) > 2:
			answer, max_score = test_knowledge(letter, k_limit, image_space, eigen_means, eigen_values, characters, weights, i)
			result += answer
		else:
			result += letter[0]
		i += 1
	print result


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("textimage", help="The PNG file to OCR", type=argparse.FileType('r'), metavar='file')
	args = parser.parse_args()

	try:
		k_limit, image_space, eigen_means, eigen_values, characters, weights = load_knowledge("./out/eigenspace.p", "./out/characters.p")
		start_ocr(args.textimage.name, k_limit, image_space, eigen_means, eigen_values, characters, weights)
	except KeyboardInterrupt:
		exit(0)
