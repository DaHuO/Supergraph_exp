#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse

if __name__ == '__main__':

	# Arguments parsing
	parser = argparse.ArgumentParser()
	parser.add_argument('-i', '--input_file', metavar='INFILE', 
                        type=argparse.FileType('r', 0), default='-',
                        help='input pancake file')
	parser.add_argument('-o', '--output_file', metavar='OUTFILE', 
                        type=argparse.FileType('w', 0), default='-',
                        help='ouput file')
	args = parser.parse_args()

	# Input file parsing
	case_max_num = int(args.input_file.readline().strip())
	case_num = 0

	for l in [l.strip() for l in args.input_file if l.strip()]:
		case_num += 1
		last_pancake = ''
		flip_num = 0
		for pancake in l:
			if not last_pancake and pancake == '-':
				flip_num += 1
			if pancake == '-' and last_pancake == '+':
				flip_num += 2
			last_pancake = pancake
		args.output_file.write("Case #{0}: {1}\n".format(case_num, flip_num))









