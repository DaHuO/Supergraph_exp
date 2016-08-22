#!/usr/bin/env python

import sys

# ==============================================================================
def read_input(filename):
	n = None
	cases = []
	with open(filename, 'r') as f:
		lines = f.read().strip().splitlines()
		n = int(lines[0])
		cases = lines[1:]
	return n, cases

# ==============================================================================
def handle_case(case):
	chars = [case[0]]
	for c in case[1:]:
		if c >= chars[0]:
			chars.insert(0, c)
		else:
			chars.append(c)
	return ''.join(chars)

# ==============================================================================
def main(filename):
	n, cases = read_input(filename)

	assert n == len(cases)

	with open('out.txt', 'w') as out:
		for i, case in enumerate(cases):
			result = handle_case(case)

			#print i + 1, case, result

			out.write('Case #{}: {}\n'.format(i + 1, result))

# ==============================================================================
if __name__ == '__main__':
	main(*sys.argv[1:])
