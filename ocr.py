#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import os
import math
from PIL import Image


def read_image(filename):
	if not os.path.exists(filename):
		return 0, []

	png_image = Image.open(filename)
	png_image.thumbnail((32, 32), Image.ANTIALIAS)
	png_width, png_height = png_image.size
	png_array = [0 for i in xrange(png_width * png_height)]

	col = 0
	for pixel in list(png_image.getdata()):
		if png_image.mode == 'L':
			pixelr = pixel
			png_pixel = pixelr
		elif png_image.mode == 'RGB':
			pixelr, pixelg, pixelb = pixel
			png_pixel = math.floor((pixelr + pixelg + pixelb) / 3)
		elif png_image.mode == 'RGBA':
			pixelr, pixelg, pixelb, pixela = pixel
			png_pixel = math.floor((pixelr + pixelg + pixelb) / 3)

		png_array[col] = int(png_pixel)
		col += 1

	image_name = os.path.splitext(os.path.basename(filename))[0]
	letter, letter_case = image_name.split('_')
	return letter, png_array


def load_knowledge(knowledge_directory, knowledge_filter=".png"):
	knowledge = []
	for filename in os.listdir(knowledge_directory):
		if filename.endswith(knowledge_filter):
			full_filename = knowledge_directory + '/' + filename
			knowledge.append(read_image(full_filename))
	return knowledge


def test_knowledge(knowledge, question):
	scores = []
	for fact_info in knowledge:
		fact = fact_info[1]
		numerator = 0
		denominatorA = 0
		denominatorB = 0
		for index, feature in enumerate(fact):
			numerator += question[index] * fact[index]
			denominatorA += question[index] * question[index]
			denominatorB += fact[index] * fact[index]
		
		if denominatorA and denominatorB:
			total_score = numerator / (math.sqrt(denominatorA) * math.sqrt(denominatorB))
		else:
			total_score = 0

		scores.append(total_score)
		
	max_score = 0
	max_score_spot = -1
	for index, score in enumerate(scores):
		if score > max_score:
			max_score = score
			max_score_spot = index
	
	answer_info = knowledge[max_score_spot]
	answer = answer_info[0]
	return answer, max_score


def write_image_to_file(eigen_image, target_file):
	width = len(eigen_image[0])
	height = len(eigen_image)
	tmp_image = Image.new('L', (width, height))
	
	#print " >>>", width, "x", height
	row = 0
	col = 0
	for i in eigen_image:
		for j in i:
			if col >= width:
				row += 1
				col = 0
			# pixelval = int(eigen_image[row][col])
			# png_image.putpixel((row, col), pixelval)
			#print col, row, "=", int(eigen_image[row][col])
			tmp_image.putpixel((col, row), int(eigen_image[row][col]))
			col += 1

	png_image = tmp_image.resize((32, 32))
	png_image.save(target_file)


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

	png_image = tmp_image.resize((32, 32))

	png_array = [0 for i in xrange(32 * 32)]
	png_image.save(target_file)
	for index, pixel in enumerate(png_image.getdata()):
		png_array[index] = int(pixel)
	return png_array


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


def unwrap_image(image_matrix):
	width = len(image_matrix[0])
	height = len(image_matrix)
	new_width = height
	new_height = width

	new_image_matrix = [0 for i in xrange(width * height)]

	for col in xrange(0, width):
		for row in xrange(0, height):
			new_image_matrix[(row * width) + col] = image_matrix[row][col]

	return new_image_matrix


def split_characters(text_row, threshhold, row_index):
	row_count = len(text_row)
	column_count = len(text_row[0])
	characters = []

	text_cols = []
	blank_col = True
	for col in xrange(0, column_count):
		pixel_col = []

		for row in xrange(0, row_count):
			if text_row[row][col] > threshhold:
				blank_col = False
			pixel_col.append(text_row[row][col])

		if not blank_col:
			text_cols.append(pixel_col)
			blank_col = True
			
		else:
			if len(text_cols):
				#characters.append(unwrap_image(text_cols))
				
				filename = "./out/img_" + str(row_index) + "-" + str(col) + ".png"
				# write_image_to_file(transpose_image(text_cols), filename)
				
				results = size_character(transpose_image(text_cols), filename)
				characters.append(results)
				text_cols = []

	return characters


def find_characters(image_matrix, depth):
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
				text_rows = []
	return characters


def read_and_split(filename):
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
		elif png_image.mode == 'RGB':
			pixelr, pixelg, pixelb = pixel
			png_pixel = math.floor((pixelr + pixelg + pixelb) / 3)
		elif png_image.mode == 'RGBA':
			pixelr, pixelg, pixelb, pixela = pixel
			png_pixel = math.floor((pixelr + pixelg + pixelb) / 3)

		png_array[row][col] = int(png_pixel)
		col += 1

	return find_characters(png_array, png_depth)


def start_ocr(knowledge, text_image):
	if not os.path.exists(text_image):
		return 0

	letters = read_and_split(text_image)
	for letter in letters:
		answer, max_score = test_knowledge(knowledge, letter)
		print answer,



if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("knowledge_base", help="Directory containing training files", action="store")
	parser.add_argument("textimage", help="The desintation PNG file", type=argparse.FileType('r'), metavar='file')
	args = parser.parse_args()

	try:
		knowledge = load_knowledge(args.knowledge_base)
		start_ocr(knowledge, args.textimage.name)
	except KeyboardInterrupt:
		exit(0)
