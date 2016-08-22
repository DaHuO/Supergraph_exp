#!/usr/bin/python

import numpy as np

#counts the number of sign changes
def minFlips(cakes): 
    nrChanges=0
    currSign=cakes[0]
    for c in cakes: 
        if c != currSign: 
            nrChanges=nrChanges+1
            currSign=c
    return nrChanges


inFile=open('pancakeInput.txt', 'r')
outFile=open('pancakeOutput.txt', 'w')

nrLines = int(inFile.readline())

for i, line in enumerate(inFile):
    cakes=line.strip() + "+"
    nrFlips=minFlips(cakes) #make sure that your string ends with "+"
    outFile.write("Case #"+str(i+1)+": "+str(nrFlips)+"\n")
inFile.close()
outFile.close()
