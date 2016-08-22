# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 06:38:11 2016

@author: Admin
"""

def getLastWord(tcNo,inputString,fileOut):
    inputString = inputString.upper()
    print(inputString)
    if len(set(inputString))==1:
        fileOut.write('Case #{}: {}\n'.format(tcNo,inputString))
        return
    mainString = inputString[0]
    totalStringList = list()    
    for letter in inputString[1:]:   
        
        if not totalStringList:        
            startString = ''.join([letter,mainString])
            endString = ''.join([mainString,letter])
            totalStringList.append(startString)
            totalStringList.append(endString)
            
            
        else:
            tempList = totalStringList[:]
            for permString in tempList:
                startString = ''.join([letter,permString])
                endString = ''.join([permString,letter])
                totalStringList.append(startString)
                totalStringList.append(endString)
                
    
    
    
    totalStringList = [validString for validString in totalStringList if len(validString)==len(inputString)]    
    totalStringList.sort()    
    fileOut.write('Case #{}: {}\n'.format(tcNo,totalStringList[-1]))
    
def main():
    fileOut = open(r'D:\SpyderWorkspace\CodeJamRoundOne\Results\A-small-attempt2 (1).out','w')
    fileIn = open(r'D:\SpyderWorkspace\CodeJamRoundOne\Results\A-small-attempt2 (1).in','r')
    noOfTcs = int(fileIn.readline())
    
  
    for tc in range(1,noOfTcs+1):    
        inputString = fileIn.readline().strip('\n')
        getLastWord(tc,inputString,fileOut)
    
    fileOut.flush()
    fileOut.close()
  


    
main()