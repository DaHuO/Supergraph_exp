#!/usr/bin/python
import sys

def getLastWord( input ):
	last = 0
	output = []
	output.append(input[0])
	for i in range(1, len(input)):
		pos = findPos(input[i], output)
		output.insert(pos, input[i])
	return ''.join(output)


def findPos(letter, list):
	if letter >= list[0]:
		return 0
	else:
		return len(list)

def main( argv ):
	infile = open(argv[1], 'r');
	outfile = open('output.txt', 'w');
	cases = int(infile.readline())
	for case in range(1, cases+1):
		lastNum = getLastWord(infile.readline().rstrip())
		print("Case #" + str(case) + ": " + str(lastNum), file=outfile)

if __name__ == "__main__":
    main(sys.argv)