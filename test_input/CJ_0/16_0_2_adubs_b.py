import sys

numCases = int(input())

for i in range(numCases):
	inString = input()
	inList = list(inString)
	expect = '+'
	flips = 0
	for char in reversed(inList):
		if char != expect:
			flips += 1
			if expect == '+': expect = '-'
			elif expect == '-': expect = '+'
	print("Case #" + str(i+1) + ": " + str(flips))