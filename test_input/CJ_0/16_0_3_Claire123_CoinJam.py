#!/usr/bin/env python
import numpy
from numpy import binary_repr
import math

inFile="input.txt"
cases=[]
with open(inFile) as f:
    content=f.readlines()
    caseNum=int(content[0].strip('\n'))
    for en in range(caseNum):
        oneCase=content[en+1].strip('\n')
        cases.append(oneCase)
f.close()

def translateNumber(strNum, base):
    strNum=list(strNum)
    strNum.reverse()
    transNum=0
    for en,sn in enumerate(strNum):
        transNum=transNum+int(sn)*(base**en)
    return transNum

primes=[]

def isprime(n):
    n = abs(int(n))
    if n in primes:
        return True
    if n < 2:
        return False
    if n == 2: 
        primes.append(n)
        return True    
    if not n & 1: 
        return False
    for x in range(3, int(math.sqrt(n)) + 1, 2):
        if n % x == 0:
            return False
    primes.append(n)
    return True

def getEndNum(digits):
    strNum='1'*digits
    return translateNumber(strNum,2)

def getStartNum(digits):
    strNum='1'+'0'*(digits-2)+'1'
    return translateNumber(strNum,2)

def getbinStr(num):
    binStr=str(binary_repr(num))
    return binStr

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))-set([1,n])
def getNTDivisor(num):  
    return list(factors(num))[0]

digits=int(cases[0].split(" ")[0])
resNum=int(cases[0].split(" ")[1])

cnt=0
result={}
num=getStartNum(digits)
print "Case #1:"
while num>=getStartNum(digits) and num<getEndNum(digits)+1:
    strNum=getbinStr(num)
    transBase=[]
    for base in range(2,11):
        if isprime(translateNumber(strNum,base)):
            break;
        else:
            transBase.append(getNTDivisor(translateNumber(strNum,base)))
    if len(transBase)==9:
        if cnt<resNum:
            res=''
            for l in range(len(transBase)):
                res+=str(transBase[l])+" "
            print strNum, transBase
        else:
            break;
            #result[strNum]=transBase   
        cnt=cnt+1
    num=num+2


