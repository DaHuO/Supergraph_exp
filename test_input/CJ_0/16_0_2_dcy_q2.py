# -*- coding: utf-8 -*-

def solve(pancake):
	flip_num = 0
	for i in range(1, len(pancake)):
		if pancake[i-1] != pancake[i]:
			flip_num += 1
	if pancake[-1] == '-':
		flip_num += 1
	return flip_num

def main():
	input_file = 'B-large.in.txt'
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

def str_to_int(s):
	return int(s.strip())

def str_to_int_list(s):
	return [int(x) for x in s.strip().split()]

if __name__ == '__main__':
	main()



