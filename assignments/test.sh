#!/bin/sh

py CPSC217S23A4Starter.py datasets/DataSet1.txt 1> txt/out.txt 2> txt/error.txt

diff -y txt/out.txt datasets/DataSet1-out.txt 