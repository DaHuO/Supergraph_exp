#Problem 2 for Google Code Jam 2016
#Matthew Gibson @chemiseblanc mgibs029@uottawa.ca

import sys

data = sys.stdin.readlines()

outfile = open("output.txt",'w')

for i in range(1,int(data[0])+1):
    flips = 0
    stack = data[i].strip()
    for j in range(len(stack)-1):
        if stack[j] != stack[j+1]:
            flips += 1

    if stack.endswith('-'):
        flips += 1

    outfile.write("Case #{}: {}\n".format(i,flips))

outfile.close()
