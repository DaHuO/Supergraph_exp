import sys
import math
import itertools


CASES = 0
CURRENT_CASE = 1
CASE_LINE_FORMAT = r"Case #%s: %s"


def get_input():
	with open(sys.argv[1], "rb") as fd:
		fd.readline()
		while True:
			line = fd.readline()
			if line == '':
				break 
			
			yield line.strip()

def print_case(output):
	global CURRENT_CASE
	print CASE_LINE_FORMAT % (CURRENT_CASE, output)
	CURRENT_CASE += 1


for line in get_input():
	line = list(line)
	ordered = [line[0]]


	for x in line[1:]:
		if ord(x) >= ord(ordered[0]):
			ordered.insert(0, x)
		else:
			ordered.append(x)

	print_case(''.join(ordered))








