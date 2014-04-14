#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pickle
import struct

def eigenspace_pickle_to_binary(infile, outfile):
	if os.path.exists(infile):
		print "Loading values from cache", infile
		
		eigenspace = pickle.load(open(infile, "rb"))
		k_limit = eigenspace["k_limit"]
		image_space = eigenspace["image_space"]
		eigen_values = eigenspace["eigen_values"]
		print " k_limit", k_limit
		print " dimensions", image_space.shape[1]
		print " image_space", image_space.shape
		print " eigen_values", eigen_values.shape

		print "Writing values to binary", infile
		with open(outfile, 'wb') as f:
			#f.write(struct.pack('f', float(k_limit))) # single-precision floating point number
			#f.write(struct.pack('d', float(k_limit))) # double-precision floating point number
			f.write(struct.pack('i', int(k_limit)))
			print " k_limit", k_limit, "(as int)"
			f.write(struct.pack('i', int(image_space.shape[1])))
			print " dimensions", image_space.shape[1], "(as int)"

			for i in xrange(0, k_limit):
				for j in xrange(0, image_space.shape[1]):
					# print image_space[i, j]
					f.write(struct.pack('d', image_space[i, j]))
			print " image_space", k_limit, "x", image_space.shape[1], "(as doubles)"
				
			for i in xrange(0, k_limit):
				# print eigen_values[i]
				f.write(struct.pack('d', eigen_values[i]))
			print " eigen_values", k_limit, "(as doubles)"

		print


def characters_pickle_to_binary(infile, outfile):
	if os.path.exists(infile):
		print "Loading values from cache", infile

		character_weights = pickle.load(open(infile, "rb"))
		characters = character_weights["characters"]
		weights = character_weights["weights"]
		print " characters", len(characters)
		print " weights", len(weights)
		
		print "Writing values to binary", infile
		with open(outfile, 'wb') as f:
			f.write(struct.pack('i', int(len(characters))))
			print " count", len(characters), "(as int)"

			for i in xrange(0, len(characters)):
				# print characters[i]
				f.write(struct.pack('c', characters[i]))
			print " characters", len(characters), "(as chars)"

			for i in xrange(0, len(weights)):
				# print weights[0][i]
				f.write(struct.pack('d', weights[0][i]))
			print " weights", len(weights), "(as doubles)"

		print


if __name__ == "__main__":
	try:
		eigenspace_pickle_to_binary("./out/eigenspace.p", "./out/eigenspace.bin")
		characters_pickle_to_binary("./out/characters.p", "./out/characters.bin")
	except KeyboardInterrupt:
		exit(0)