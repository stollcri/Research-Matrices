Research-Matrices
=================

Code for researching matrices and linear algebra based algorithms

svd.py -- perform Singular Value Decomposition on a black and white png file and output a png file which represents how the image would look if it were compressed at the specifiec k value (the resulting image is not actually compressed)

svd-rgb.py -- same as above except for color png images

svd-pix.py -- toy program which attempts genererate an "8-bit" version of the supplied black and white png, the image is pixelated into big blocks

svd-avg.py -- a program to experiment with averaging images together by interlacing the highest eigenvalues from two different images; it gives the first image more weight so that when it is run multiple times the least recent images begin to "fade away" (check out results/avg)

eigenimage.py -- given a set of images generate an eigenimage

gen-train.py -- generate thumbnail images for a given character (or word) for each font available on a Mac (generates 147 thumbnails per character)

ml-ocr.py -- simple machine learning optical character recogition program which can be ran in batch or interactively