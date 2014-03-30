#!/bin/bash

echo "Already nstalled libfreetype2, right?"
echo " Download it"
echo " cd freetype-2.n.m"
echo " ./configure"
echo " make"
echo " sudo make install"

export LDFLAGS=-L/usr/X11/lib
export CFLAGS=-Qunused-arguments
export CPPFLAGS=-Qunused-arguments

pip install Pillow
