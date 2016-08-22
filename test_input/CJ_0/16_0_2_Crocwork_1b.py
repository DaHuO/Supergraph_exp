from string import *
import math

def read_words(filename):
    '''
    converts a file to a list
    '''
    words = []
    for line in filename:
            words.append(line.strip())
    return words

filename = open("in.txt", 'r')
numcases = int(filename.readline().split()[0])

for case in range(numcases):
	stack = filename.readline().split()[0]

	flips = 0
	for cake in stack[::-1]:
		if (cake == "+" and flips%2==0) or (cake == "-" and flips%2 == 1):
			continue
		else:
			flips +=1
	
	print "Case #" + str(case+1) + ":", flips

