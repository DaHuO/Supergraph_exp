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
################################################################
QNO = 'b' #SET QUESTION NUMBER
FIN,FOUT = QNO+'.in.txt',QNO+'.out.txt'
FIN = QNO.capitalize()+'-small-attempt0.in'
FIN = QNO.capitalize()+'-large.in'
fin = open(FIN)
fout = open(FOUT,'w')
sys.stdin = fin
######################## PROGRAM  START ##########################

for t in range(int(input())):
    s = input()
    d = 0
    cur = s[0]
    for c in s:
        if c!=cur:
            cur = c
            d+=1
    if cur=='-': d+=1
    print("Case #{0}: {1}".format(t+1,d),file=fout)
######################## PROGRAM END #############################
fin.close()
fout.close()
print("Program complete")
