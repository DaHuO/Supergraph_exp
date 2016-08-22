import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


testfile='B-large.in'
outputfile='B-large.out'

fo = open(testfile, "rw+")
print "Name of the file: ", fo.name
firstline = fo.readline()
fo.close()
numcases=int(firstline.split('\n')[0])
print 'numcases: ',numcases
inpt=np.genfromtxt(testfile, skiprows=1, dtype=str)

def flips(S):
    stack= map(int, S.replace('+','1 ').replace('-','0 ').split(' ')[0:-1])
    if stack[-1]==0:
        flipbottom=1
    else:
        flipbottom=0
    numflips=np.sum(np.abs(np.diff(stack)))+flipbottom
    return numflips


outfile=open(outputfile, 'w')
for m,case in enumerate(inpt): 
    print '********'+str(case)+'********'
    answer=flips(case)
    print answer
    outfile.write('Case #'+str(m+1)+': '+str(answer)+'\n')
    
outfile.close()

b=2
