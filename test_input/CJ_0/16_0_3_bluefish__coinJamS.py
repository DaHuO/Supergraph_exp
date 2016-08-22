# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 19:27:27 2016

@author: Bluefish_
"""

import math
import itertools

def checkNotPrime(number,base):
    if base % 2 ==0:
        start = 3
    else:
        start = 2
    end = math.sqrt(number)
    while start<end:
        if number % start != 0:
            start+=2
        else:
            return start
    return -1

def calcBaseTen(number,base):
    sum = 0
    for i in range(len(number)):
        if number[i]!=0:
            sum+=base**i
    return sum
    
def checkCoin(digits):
    divisor = []
    for base in range(2,11):
        jamcoin = calcBaseTen(digits,base)
        temp = checkNotPrime(jamcoin,base)
        if temp!=-1:
            divisor.append(temp)
        else:
            return []
    return divisor
    
def printThisCoin(number,divisor,length,out):
    out.write("1"+number[::-1]+"1")
    for item in divisor:
        out.write(" "+str(item))
    out.write("\n")

def constructNum(string):
    temp = [1]
    for i in range(len(string)):
        temp.append(int(string[i]))
    temp.append(1)
    return temp

infile = open("C-small-attempt1.in",'r')
outfile = open("out-small-coinJam.txt",'w')
infile.readline()
string = infile.readline()
thelist = string.split(" ")
numN = int(thelist[0])
numJ = int(thelist[1])
J = 0
counter = 0
allnum = ["".join(seq) for seq in itertools.product("01", repeat=numN-2)]
outfile.write("Case #1:\n")
while (J!=numJ):
    digits = constructNum(allnum[counter])
    temp = checkCoin(digits)
    if temp!=[]:
        printThisCoin(allnum[counter],temp,numN,outfile)
        J+=1   
    counter+=1
infile.close()
outfile.close()
    