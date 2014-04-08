#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import string
from PIL import Image, ImageFont, ImageDraw

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
				return i
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
				return j
	return height


def gen_filename(outputdirectory, character_in, index):
	if character_in == '.':
		character = '001'
	elif character_in == ',':
		character = '002'
	elif character_in == '?':
		character = '003'
	elif character_in == '!':
		character = '004'
	elif character_in == '-':
		character = '005'
	elif character_in == '_':
		character = '006'
	elif character_in == '#':
		character = '007'
	elif character_in == '@':
		character = '008'
	elif character_in == ';':
		character = '009'
	elif character_in == '\'':
		character = '010'
	elif character_in == '"':
		character = '011'
	else:
		character = character_in

	if character.isupper():
		character_case = 'u'
	elif character.islower():
		character_case = 'l'
	else:
		character_case = 'n'

	dirtyfilename = character + '_' + character_case + '-' + index + ".png"
	directoryname = outputdirectory + '/'

	valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
	filename = ''.join(c for c in dirtyfilename if c in valid_chars)
	
	return directoryname + filename


def gen_images(character, outputdirectory):
	font_list = {"AmericanTypewriter.ttc","Andale Mono.ttf","Apple Chancery.ttf","Apple LiGothic Medium.ttf","Apple LiSung Light.ttf","AppleGothic.ttf","AppleMyungjo.ttf","AppleSDGothicNeo-ExtraBold.otf","AppleSDGothicNeo-Heavy.otf","AppleSDGothicNeo-Light.otf","AppleSDGothicNeo-Medium.otf","AppleSDGothicNeo-SemiBold.otf","AppleSDGothicNeo-Thin.otf","AppleSDGothicNeo-UltraLight.otf","Arial Black.ttf","Arial Bold Italic.ttf","Arial Bold.ttf","Arial Italic.ttf","Arial Narrow Bold Italic.ttf","Arial Narrow Bold.ttf","Arial Narrow Italic.ttf","Arial Narrow.ttf","Arial Rounded Bold.ttf","Arial Unicode.ttf","Arial.ttf","Athelas.ttc","Ayuthaya.ttf","Bangla MN.ttc","Bangla Sangam MN.ttc","Baoli.ttc","Baskerville.ttc","BiauKai.ttf","BigCaslon.ttf","Brush Script.ttf","Chalkboard.ttc","ChalkboardSE.ttc","Chalkduster.ttf","CharcoalCY.dfont","Charter.ttc","Cochin.ttc","Comic Sans MS Bold.ttf","Comic Sans MS.ttf","Copperplate.ttc","Courier New Bold Italic.ttf","Courier New Bold.ttf","Courier New Italic.ttf","Courier New.ttf","DIN Alternate Bold.ttf","DIN Condensed Bold.ttf","Devanagari Sangam MN.ttc","Didot.ttc","EuphemiaCAS.ttc","Futura.ttc","GenevaCY.dfont","Georgia Bold Italic.ttf","Georgia Bold.ttf","Georgia Italic.ttf","Georgia.ttf","GillSans.ttc","Gujarati Sangam MN.ttc","Gungseouche.ttf","Gurmukhi MN.ttc","Gurmukhi Sangam MN.ttc","Hannotate.ttc","Hanzipen.ttc","HeadlineA.ttf","Hei.ttf","HelveticaCY.dfont","Herculanum.ttf","Hiragino Sans GB W3.otf","Hiragino Sans GB W6.otf","Hoefler Text.ttc","Impact.ttf","InaiMathi.ttf","Iowan Old Style.ttc","Kai.ttf","Kaiti.ttc","Kannada MN.ttc","Kannada Sangam MN.ttc","Kefa.ttc","Khmer MN.ttc","Khmer Sangam MN.ttf","Krungthep.ttf","Lantinghei.ttc","Lao Sangam MN.ttf","Libian.ttc","Malayalam MN.ttc","Malayalam Sangam MN.ttc","Marion.ttc","Microsoft Sans Serif.ttf","NanumGothic.ttc","NanumMyeongjo.ttc","NanumScript.ttc","Oriya MN.ttc","Oriya Sangam MN.ttc","Osaka.ttf","OsakaMono.ttf","PCmyoungjo.ttf","PTMono.ttc","PTSans.ttc","PTSerif.ttc","PTSerifCaption.ttc","Papyrus.ttc","Pilgiche.ttf","PlantagenetCherokee.ttf","Sathu.ttf","Savoye LET.ttc","Seravek.ttc","Silom.ttf","Sinhala MN.ttc","Sinhala Sangam MN.ttc","Skia.ttf","SnellRoundhand.ttc","Songti.ttc","SuperClarendon.ttc","Tahoma Bold.ttf","Tahoma.ttf","Tamil MN.ttc","Tamil Sangam MN.ttc","Telugu MN.ttc","Telugu Sangam MN.ttc","Times New Roman Bold Italic.ttf","Times New Roman Bold.ttf","Times New Roman Italic.ttf","Times New Roman.ttf","Trebuchet MS Bold Italic.ttf","Trebuchet MS Bold.ttf","Trebuchet MS Italic.ttf","Trebuchet MS.ttf","Verdana Bold Italic.ttf","Verdana Bold.ttf","Verdana Italic.ttf","Verdana.ttf","WawaSC-Regular.otf","WawaTC-Regular.otf","WeibeiSC-Bold.otf","WeibeiTC-Bold.otf","Xingkai.ttc","Yu Gothic Bold.otf","Yu Gothic Medium.otf","Yu Mincho Demibold.otf","Yu Mincho Medium.otf","Yuanti.ttc","YuppySC-Regular.otf","YuppyTC-Regular.otf","Zapfino.ttf"}
	font_location = "/Library/Fonts/"
	fill_color = "#000000"
	text_color = "#ffffff"
	image_size_work = 128
	image_size_final = 32
	image_depth = 255

	for index, font_name in enumerate(font_list):
		new_image = Image.new('L', (image_size_work, image_size_work))
		new_draw = ImageDraw.Draw(new_image)

		# draw the background
		new_draw.rectangle(((0, 0), (image_size_work, image_size_work)), fill_color)

		# draw the character
		font_path = font_location + font_name
		text_font = ImageFont.truetype(font_path, 72)
		new_draw.text((8, 8), character+' ', text_color, text_font)

		# remove excess border
		x_left = find_crop_left(new_image, image_size_work, image_size_work, image_depth)
		x_right = find_crop_right(new_image, image_size_work, image_size_work, image_depth)
		y_top = find_crop_top(new_image, image_size_work, image_size_work, image_depth)
		y_bottom = find_crop_bottom(new_image, image_size_work, image_size_work, image_depth)
		tmp_image = new_image.crop((x_left-1, y_top-1, x_right+2, y_bottom+2))

		# fit character to final image size
		png_image = tmp_image.resize((image_size_final, image_size_final))
		#
		# USING THE LINE ABOVE (TESTING AGAINST TRAINING SET)
		#  (upper case only)
		#   3354 / 3796.0 = 88.3561643836
		#   3354 / 3796.0 = 88.3561643836
		#  (upper, lower, numbers)
		#   6896 / 9052.0 = 76.1820592134
		#   7951 / 9052.0 = 87.8369421122
		# USING THE LINES BELOW (TESTING AGAINST TRAINING SET)
		#  (upper case only)
		#   3277 / 3796.0 = 86.3277133825
		#   3277 / 3796.0 = 86.3277133825
		#
		# TODO: Check if certain letters perform better using one technique
		#
		# tmp_image.thumbnail((image_size_final-2, image_size_final-2), Image.ANTIALIAS)
		# png_image = Image.new('L', (image_size_final, image_size_final))
		# new_draw = ImageDraw.Draw(png_image)
		# new_draw.rectangle(((0, 0), (image_size_final, image_size_final)), fill_color)
		# width, height = tmp_image.size
		# originx = int((image_size_final - width) / 2)
		# originy = int((image_size_final - height) / 2)
		# png_image.paste(tmp_image, (originx, originy, originx+width, originy+height))

		# save the image
		filename = gen_filename(outputdirectory, character, str(index))
		png_image.save(filename)
		#print filename, "\t<", font_name


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("character", help="The character to generate images for", action="store")
	parser.add_argument("outputdirectory", help="Where to store the image files", action="store")
	args = parser.parse_args()

	try:
		gen_images(args.character, args.outputdirectory)
	except KeyboardInterrupt:
		exit(0)
