import numpy as np
import fileinput

l = []

for i in fileinput.input():
	if i:
		l.append((i.replace("\n","")))

# print l

#remove # test cases
l = l[1:]

caseNum = 1 
for curr in l:
	stack = list(curr)
	stack = stack[::-1]
	# print stack

	moves = 0
	old_move = 0
	for i in range(len(stack)):

		if i == 0:
			if stack[i] == '-':
				moves += 1
				old_move = '-'
			else:
				old_move = '+'
		else:
			if old_move != stack[i]:
				moves += 1
				old_move = stack[i]
			

	print "Case #%s: %s" %(caseNum,moves)
	caseNum += 1

