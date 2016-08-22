# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 10:35:52 2016

@author: Admin
"""
from collections import defaultdict
import math

def getBaseNumber(number,base):
    numberStrList = list(str(number))
    resultNumber = 0
    strLen = len(numberStrList)-1
    for index,digit in enumerate(numberStrList):
        resultNumber+= (base**(strLen-index)) * (int(digit))
    return resultNumber

def isPrime(number):    
    if number<2:
        return 0
    if number<=3:
        return True
        
    flag = 1
#    i=5
#    while i*i<=int(math.sqrt(number)):
#        if number%i==0 or number%(i+2)==0:
#            flag = 0
#        i+=6
    for i in range(2,99999):
        if number%i==0:
            flag =0
            break
    return flag
    

def getDivisor(number):   
    for i in range(2,99999):
        if number%i==0:
            return i

def jamCoinNumbers(tcNo,N,J,fileOut):
    coinNumbersList = list()
    basesList = [2,3,4,5,6,7,8,9,10] 
    jamCoinDict = defaultdict(list)        
    
    for step in range(0,int(((2**32)-(2**31))/J),J):
        
        coinNumbersList = list()
        for i in range((2**31)+step,(2**31)+J+step):
            binRep = str(bin(i)[2:])        
            if binRep[0]=='1' and binRep[-1]=='1':                
                coinNumbersList.append(binRep.zfill(32))        
       
        for eachNumber in coinNumbersList:            
            for base in basesList:                
                baseNo = getBaseNumber(eachNumber,base)                
                if isPrime(baseNo):
                    if jamCoinDict.get(eachNumber):
                        jamCoinDict.pop(eachNumber)
                    break
                else:
                    tempNo = getDivisor(baseNo)
                    jamCoinDict[eachNumber].append(str(getBaseNumber(tempNo,10)))
            if len(jamCoinDict.keys())==J:
                break
            else:
                continue
        if len(jamCoinDict.keys())==J:
            break
        else:
            continue
    fileOut.write('Case #{}:\n'.format(tcNo))
    
    for key,value in jamCoinDict.items():
        fileOut.write('{} {}\n'.format(key,' '.join(value)))

def main():
    fileOut = open(r'D:\SpyderWorkspace\CodeJam\CodeJam16Results\LargeCoinJam.txt','w')
    fileIn = open(r'D:\SpyderWorkspace\CodeJam\CodeJam16Results\C-large.in','r')
    
    noOfTcs = int(fileIn.readline())
    N,J = fileIn.readline().strip('\n').split()
    jamCoinNumbers(noOfTcs,int(N),int(J),fileOut)
    
    
    fileOut.flush()
    fileOut.close()
    fileIn.close()

main()









