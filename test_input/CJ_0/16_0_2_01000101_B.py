import os, sys
import math, itertools, random

# get problem letter from script name
problem_letter = sys.argv[0].split('.')[0]
data_set = sys.argv[1]
attempt_number = sys.argv[2]

input_filename = "%s-%s-%s.in" % (problem_letter, data_set, attempt_number)
input_file = open(input_filename)
lines = [line[:-1] for line in input_file.readlines()[1:]][:]

output_filename = "%s.out" % problem_letter
output_file = open(output_filename, "w+")
sys.stdout = output_file

def get_chunks(lines, n):
	for i in range(0, len(lines), n):
		yield lines[i:i+n]

def get_answer(chunk):
	stack = list(chunk[0])
	time = 0
	while "-" in stack:

		top = stack[0]

		if top == "+":
			opposite = "-"

		else:
			opposite = "+"

		if len(stack) == 1:
			return 1

		for i in range(len(stack)):
			if stack[i] == top:
				stack[i] = opposite
			else:
				break

		time += 1
		
	return time

lines_per_case = 1
chunks = get_chunks(lines, lines_per_case)

for i, chunk in enumerate(chunks):
	print "Case #%s: %s" % (i+1, get_answer(chunk))
