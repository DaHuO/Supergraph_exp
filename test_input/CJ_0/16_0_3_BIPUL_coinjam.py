############### Author: Bipul Ranjan @ranjanbipul ###############
import sys
import time
import os
import math
import operator
import random
from functools import lru_cache
from decimal import Decimal as D
from fractions import Fraction as F
#sys.setrecursionlimit(10000)
#@lru_cache(maxsize=None)
MOD = 1000000007
######################## PROGRAM  START ##########################
p = [[pow(i,j) for j in range(32)] for i in range(11)]
def myint(s,b):
    l = len(s)
    num = 0
    for i in range(l):
            if s[i]=='1': num+=p[b][l-i-1]
    return num

for k in range(32,2,-1):
    print("start "+str(k))
    fout = open('c.'+str(k)+'.out.txt','w')
    print("Case 1:",file=fout)
    num,start,end=0,pow(2,k-1)+1,pow(2,k)
    while num < 500 and start<end:
        out = [0 for i in range(11)]
        s = str(bin(start))[2:]
        for i in range(2,11):
            n = myint(s,i)
            for j in range(2,min(math.ceil(math.sqrt(n)),100000)):
                if not n%j:
                    out[i] = j
                    break
            if not out[i]:
                break
        if out[10]:
            print("{0} {1}".format(s," ".join([str(h) for h in out[2:]])),file=fout)
            num+=1
        print('.',end="")
        start+=2
    print("end "+str(k))    
    fout.close()
######################## PROGRAM END #############################
print("Program complete")
