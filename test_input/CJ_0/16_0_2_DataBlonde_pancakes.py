# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 15:10:54 2016

@author: marinasergeeva
"""
from sys import stdin

def getNumberOfFlips(pancakes):
    res = 0
    curEl = pancakes[0]
    for el in pancakes:
        if el != curEl:
            res += 1
            curEl = el
    if pancakes[-1] == "-":
        res += 1
    return res
    
def main():
    numCases = int(stdin.readline().strip())
    for i in range(1, numCases + 1):        
        pancakes = stdin.readline().strip()
        print "Case #{0}: {1}".format(i, getNumberOfFlips(pancakes))
        
if __name__ == "__main__":
    main()