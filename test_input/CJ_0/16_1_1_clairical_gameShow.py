import sys, os
import fileinput
import math



def getString(file):
    n = int(file.readline())
    for i in range(n):
        finalStr = ""
        stri = file.readline().rstrip()
        for s in stri:
            if len(finalStr) == 0:
                finalStr = s
                continue
            firstLetter = finalStr[0]
            if s >= firstLetter:
                finalStr = s + finalStr
            else:
                finalStr = finalStr + s
        print "Case #" + str(i+1) + ": " + finalStr


if __name__ == '__main__':
    f = open(sys.argv[1], 'r')
    getString(f)
    f.close()