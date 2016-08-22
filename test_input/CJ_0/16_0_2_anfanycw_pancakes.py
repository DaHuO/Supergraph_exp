#!/usr/bin/python
from __future__ import print_function

outfile = None
stack = []
size = 0

def run():
	global outfile
	outfile = open("output.txt", "w")

	with open("input.txt", "r") as f:
		lines = []
		for line in f:
			lines.append(line.strip("\n"))

		lines = lines[1:]

		for i,l in enumerate(lines):
			flip_pancakes(i+1, str(l))


def flip_pancakes(case, tc):
	global stack, size, outfile

	stack = map(str, tc)
	size = len(stack)

	flips = 0
	last_flip = False
	for i, p in enumerate(stack):
		if i == (size-1):
			if p == '-':
				last_flip = True
			break

		if p != stack[i+1]:
			flips += 1

	if last_flip:
		flips += 1
	print("Case #%d: %d" % (case, flips), file=outfile)

run()