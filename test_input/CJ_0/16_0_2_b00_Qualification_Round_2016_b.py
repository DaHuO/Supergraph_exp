#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  Qualification_Round_2016_b.py
#
#  Copyright 2016 nerio
#
#

import fileinput

def lift_n_flip(p_stack):
	if '+' in p_stack and '-' not in p_stack:
		return 0
	elif '+' not in p_stack and '-' in p_stack:
		return 1
	else:
		# Index of bottommost blank side up pancake
		bbp_index = p_stack.rfind('-')
		p_stack = list(p_stack[0:bbp_index])
		
		curr_p_side = '-'
		sp_count = 0
		while p_stack:
			next_p_side = p_stack.pop()
			if next_p_side != curr_p_side:
				sp_count += 1
				curr_p_side = next_p_side
		
		return sp_count + 1

def main():

	curr_t_case = 1
	first_line = True
	for line in fileinput.input():
		line = line.strip()
		
		if first_line:
			t_cases = int(line)
			first_line = False
			continue
		
		result = lift_n_flip(line)
			
		print('Case #', curr_t_case ,': ', result, sep='')
		curr_t_case += 1

	return 0

if __name__ == '__main__':
	main()
