#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import string
from PIL import Image, ImageFont, ImageDraw

def find_crop_left(image, width, height):
	found_fg_start = False
	for i in range(width):
		for j in range(height):
			if image.getpixel((i,j)) == 0:
				found_fg_start = True
				return i
	return 0


def find_crop_right(image, width, height):
	found_fg_start = False
	for i in range(width-1,0,-1):
		for j in range(height):
			if image.getpixel((i,j)) == 0:
				found_fg_start = True
				return i
	return width


def find_crop_top(image, width, height):
	found_fg_start = False
	for j in range(height):
		for i in range(width):
			if image.getpixel((i,j)) == 0:
				found_fg_start = True
				return j
	return 0


def find_crop_bottom(image, width, height):
	found_fg_start = False
	for j in range(height-1,0,-1):
		for i in range(width):
			if image.getpixel((i,j)) == 0:
				found_fg_start = True
				return j
	return height


def gen_filename(outputdirectory, character, index):
	valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
	dirtyfilename = character + "-" + index + ".png"
	directoryname = outputdirectory + '/'
	filename = ''.join(c for c in dirtyfilename if c in valid_chars)
	return directoryname + filename


def gen_images(character, outputdirectory):
	font_list = {"charI24.pil", "charR24.pil", "courB24.pil", "courBO24.pil", "courO24.pil", "courR24.pil", "helvB24.pil", "helvBO24.pil", "helvO24.pil", "helvR24.pil", "luBIS24.pil", "luBS24.pil", "luIS24.pil", "luRS24.pil", "lubB24.pil", "lubBI24.pil", "lubI24.pil", "lubR24.pil", "lutBS24.pil", "lutRS24.pil", "ncenB24.pil", "ncenBI24.pil", "ncenI24.pil", "ncenR24.pil", "timB24.pil", "timBI24.pil", "timI24.pil", "timR24.pil"}
	font_location = "./img/fonts/"
	fill_color = "#ffffff"
	text_color = "#000000"
	image_size = 48

	for index, font_name in enumerate(font_list):
		new_image = Image.new('L', (image_size, image_size))
		new_draw = ImageDraw.Draw(new_image)

		# draw the background
		new_draw.rectangle(((0, 0), (image_size, image_size)), fill_color)

		# draw the character
		font_path = font_location + font_name
		text_font = ImageFont.load(font_path)
		new_draw.text((4, 4), character+' ', text_color, text_font)

		# remove excess border and resize
		x_left = find_crop_left(new_image, image_size, image_size)
		x_right = find_crop_right(new_image, image_size, image_size)
		y_top = find_crop_top(new_image, image_size, image_size)
		y_bottom = find_crop_bottom(new_image, image_size, image_size)
		tmp_image = new_image.crop((x_left-1, y_top-1, x_right+2, y_bottom+2))
		png_image = tmp_image.resize((image_size, image_size))

		# save the image
		filename = gen_filename(outputdirectory, character, str(index))
		png_image.save(filename)


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("character", help="The character to generate images for", action="store")
	parser.add_argument("outputdirectory", help="Where to store the image files", action="store")
	args = parser.parse_args()

	try:
		gen_images(args.character, args.outputdirectory)
	except KeyboardInterrupt:
		exit(0)
