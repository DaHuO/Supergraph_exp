#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  Round_1a_2016_a.py
#
#  Copyright 2016 nerio
#
#

import fileinput

def last_word(S):
	words = []
	
	for W in S:
		words_tmp = []
		if words:
			while words:
				curr_W = words.pop()
				left_W = curr_W + W
				right_W = W + curr_W
				words_tmp.append(left_W)
				words_tmp.append(right_W)
				
			words.extend(words_tmp)
		else:
			words.append(S[0])
	
	words.sort()
	return words[-1]

def main():

	curr_t_case = 1
	first_line = True
	for line in fileinput.input():
		line = line.strip()
		
		if first_line:
			t_cases = int(line)
			first_line = False
			continue
		
		result = last_word(line)
			
		print('Case #', curr_t_case ,': ', result, sep='')
		curr_t_case += 1

	return 0

if __name__ == '__main__':
	main()
