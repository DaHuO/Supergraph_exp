# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 15:45:58 2016

@author: marinasergeeva
"""
from sys import stdin
from itertools import product

def getJamcoins(length, number):
    # 2^6 > 50 => will have enough combinations of 11 and 00 to get jamcoins
    multipliers = " ".join([str(int("11", i)) for i in range(2, 11)])
    for numberPart in product(["11", "00"], repeat=(length - 4) / 2):
        curNumber = "11" + "".join(numberPart) + "11"
        print curNumber + " " + multipliers
        number -= 1
        if number == 0:
            break
        

def main():
    numCases = int(stdin.readline().strip())
    for i in range(1, numCases + 1):        
        [length, number] = [int(s) for s in stdin.readline().strip().split()]
        print "Case #{0}:".format(i)
        getJamcoins(length, number)        
        
if __name__ == "__main__":
    main()