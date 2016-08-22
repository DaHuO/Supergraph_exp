import sys
import os

output_format = 'Case #{0}: {1}'
# riddle #1
def solve_riddle(input):
	stri = input
	res = input[0]
	for i in range(1,len(input)):
		c = input[i]
		if c >= res[0]:
			res = c + res
		else:
			res = res + c
	return res

# read the input
file = open(sys.argv[1])
output = open('output.txt', 'w')
lines = file.readlines()
# the number of cases.
n = int(lines[0])
cur_line = 1
# solve the riddle and write to the output file.
for i in range(n):
	answer = solve_riddle(lines[i+1])
	output.write(output_format.format(i+1,answer))