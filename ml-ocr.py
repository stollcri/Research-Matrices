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
	return image_name, png_array


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
		in_common = 0
		for index, feature in enumerate(fact):
			if question[index] == fact[index]:
				in_common += 1
		scores.append(in_common)
	
	max_score = 0
	max_score_spot = -1
	for index, score in enumerate(scores):
		if score > max_score:
			max_score = score
			max_score_spot = index
	
	answer_info = knowledge[max_score_spot]
	answer = answer_info[0]
	return answer


def start_batch_mode(knowledge, directory, batch_filter=".png"):
	for filename in os.listdir(directory):
		if filename.endswith(batch_filter):
			full_filename = directory + '/' + filename
			question_info = read_image(full_filename)
			question = question_info[1]
			if question:
				answer = test_knowledge(knowledge, question)
				print filename, "\t=>", answer


def start_interactive_mode(knowledge):
	cmd = ''
	while cmd != "x" and cmd != "exit":
		cmd = raw_input("Enter file to test or 'exit': ")
		if cmd != "x" and cmd != "exit":
			question_info = read_image(cmd)
			question = question_info[1]
			if question:
				answer = test_knowledge(knowledge, question)
				print " That is:", answer


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("knowledge_base", help="Directory containing training files", action="store")
	
	parser.add_argument("-b", "--batch", help="Run batch mode", action="store_true")
	parser.add_argument("batch_directory", help="Batch mode directory", nargs='?', default=os.getcwd())
	args = parser.parse_args()

	try:
		knowledge = load_knowledge(args.knowledge_base)
		if args.batch:
			start_batch_mode(knowledge, args.batch_directory)
		else:
			start_interactive_mode(knowledge)

	except KeyboardInterrupt:
		exit(0)
