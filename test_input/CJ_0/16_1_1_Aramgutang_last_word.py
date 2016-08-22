#!/usr/bin/env python

import sys

def arrange(letters):
	largest = sorted(letters)[-1]
	indices = [index for index, letter in enumerate(letters) if letter == largest]
	arranged = largest * len(indices)
	if len(indices) < len(letters):
		indices = [-1] + indices + [len(letters)]
		for i in range(len(indices) - 1):
			if indices[i+1] - indices[i] > 1:
				segment = letters[indices[i]+1:indices[i+1]]
				if indices[i] == -1:
					arranged += arrange(segment)
				else:
					arranged += segment
	return arranged

with open(sys.argv[1]) as input:
	input.next()
	for case, line in enumerate(input, 1):
		answer = arrange(line.strip())
		print 'Case #%s: %s' % (case, answer)