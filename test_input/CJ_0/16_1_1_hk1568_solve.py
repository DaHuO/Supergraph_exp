#!/usr/bin/env python
import sys


def lastW(letters):
    
    rlt=letters[0]
    for i in letters[1:]:
        if rlt[0] > i:
            rlt = rlt + i 
        else:
            rlt = i + rlt 

    return rlt
    

fin = open(sys.argv[1], 'r')
cases = int( fin.readline().strip() )
for i  in range(cases):
    letters = fin.readline().strip()
    print "Case #%d: %s" % ( i+1 , lastW(letters) )
