# -*- coding: utf-8 -*-

import pdb
from collections import deque

def solve(s):
	if len(s) == 0:
		return ''
	d = deque(s[0])
	for i in range(1, len(s)):
		if s[i] >= d[0]:
			d.appendleft(s[i])
		else:
			d.append(s[i])
	return ''.join(list(d))

def main():
	# pdb.set_trace()

	input_file = 'A-large.in.txt'
	output_file = 'out'
	output_format = 'Case #{0}: {1}\n'

	results = []

	with open(input_file, 'r') as f:
		case_total = str_to_int(f.readline())
		# for each case:
		for i in range(case_total):
			# some code . reading
			line = f.readline().strip()
			results.append(solve(line))
			
	with open(output_file, 'w') as f:
		for i in range(len(results)):
			# for each result
			f.write(output_format.format(i+1, results[i]))	


# --------------------------------------------

# '1\n' => 1
def str_to_int(s):
    return int(s.strip())

# '1 2 3' => [1, 2, 3]
def str_to_int_list(s, delimiter = ' '):
    return [int(x) for x in s.strip().split(delimiter)]

if __name__ == '__main__':
	main()



