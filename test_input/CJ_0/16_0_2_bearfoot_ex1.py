#! /usr/bin/python

import sys
import math

if len(sys.argv) < 2:
	exit(1)

finname = sys.argv[1]
foutname = finname.replace(".in",".out")

print "{} {}".format(finname,foutname)

fin=open(finname,"r")
fout=open(foutname,"w")

numcases=int(fin.readline());

print numcases

for case in range(0,numcases):
    fout.write ("Case #%d: " % (case+1))
    line=fin.readline().strip()
    length=len(line)-1
    line += '+'
    char= 'a'
    swaps=0
    for i in range(length,-1,-1):
        #print "line[%d]: %c, line[%d]: %c" % (i,line[i],i+1,line[i+1])
        if line[i] != line[i+1]:
            swaps+=1;
    print "line: %s, len: %d, 0th char: %c, swaps: %d" % (line,length,line[0],swaps)
    fout.write("%d\n" % swaps)
		

