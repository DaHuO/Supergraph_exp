#!/usr/bin/env python
import sys

S = ''

def process(S):
	t1 = ''
	t2 = ''
	rlt= ''
	for i in S:
		t1 = rlt + i
		t2 = i + rlt
		if t1 > t2 :
			rlt = t1
		else:
			rlt = t2
	return rlt

input_file = open(sys.argv[1], 'r')
T = int(input_file.readline())
for i in range(T):
	S = input_file.readline().strip()
	print 'Case #%d: ' % (i + 1), process(S)