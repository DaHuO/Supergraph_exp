import sys, os
import fileinput
import math



def getMoves(file):
    n = int(file.readline())
    for i in range(n):
        line = file.readline().rstrip()
        numMoves = 0
        curVal = line[0]
        for char in line:
            if (curVal != char):
                numMoves +=1
                curVal = char
        if curVal == '-':
            numMoves +=1
        print "Case #" + str(i+1) + ": " + str(numMoves)









if __name__ == '__main__':
    f = open(sys.argv[1], 'r')
    getMoves(f)
    f.close()