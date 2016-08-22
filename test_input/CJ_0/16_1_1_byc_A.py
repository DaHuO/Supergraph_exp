#!/usr/bin/python3
import sys

file_prefix = 'A-large'

filein = open(file_prefix + '.in')
fileout = sys.stdout if 'sample' in file_prefix else open(file_prefix + '.out', 'w')
linein = lambda: filein.readline().strip()
lineout = lambda s: fileout.write(s + '\n')

ncases = int(linein())

for case in range(ncases):
	chars = linein()
	out_str = ""
	largest_char = None
	for c in chars:
		if largest_char is None or c >= largest_char:
			out_str = c + out_str
			largest_char = c
		else:
			out_str = out_str + c


	lineout("Case #{0}: {1}".format(case + 1, out_str))
