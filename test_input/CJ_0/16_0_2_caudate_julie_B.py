# April, 10, 2016
# Qualification Round
# "Revenge of the Pancakes"

from time import time
from math import sqrt

#inpath = "B-sample.in"
inpath = "B-large.in"
#inpath = 'B-small-attempt0.in'
outpath = "B.out"

def Smiles(pancakes):
    count = 1
    for i in range(1, len(pancakes)):
        if not pancakes[i] == pancakes[i - 1]:
            count += 1
    if pancakes[-1] == '+':
        count -= 1
    return count        
    
timestart = time()

fin = open(inpath)
fout = open(outpath, 'w')

T = int(fin.readline())
for case in range(1, T+1):
    pancakes = fin.readline().strip("\n")
    #print Smiles(pancakes)
    fout.write("Case #%d: %d\n" % (case, Smiles(pancakes)))
    
fin.close()
fout.close()
print "%.4f" % (time() - timestart)
