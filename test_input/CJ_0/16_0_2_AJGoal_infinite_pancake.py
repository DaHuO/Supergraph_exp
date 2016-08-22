# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 13:26:49 2016

@author: Admin
"""

def flipStr(inputStrList):
    
    inputStrList.reverse()
    finalList = list()
    for st in inputStrList:
        if st=='+':
            finalList.append('-')
        else:
            finalList.append('+')
    return finalList
        

def getOptimumFlips(tcNo,inputStr,fileOut):
    
    flipCount=0    
    cutOff = 99999
    if '-' not in inputStr:
        fileOut.write('Case #{}: {}\n'.format(tcNo,0))
        return
    if '+' not in inputStr:
        fileOut.write('Case #{}: {}\n'.format(tcNo,1))
        return
    panCakeStrList = list(inputStr)
    validStr = '+'*len(inputStr)
    start = 0
    counter=0
    end = len(panCakeStrList)-1
    while True and counter<cutOff:
       
        if panCakeStrList[end]=='-':
          
            if '-' in panCakeStrList[start:end]:                
                if panCakeStrList[start]=='+':
                    temp = start
                    plusCount=0
                    while temp<end:
                        if panCakeStrList[temp]=='-':
                            break
                        if panCakeStrList[temp]=='+':
                            plusCount+=1
                        temp+=1
                    panCakeStrList[start:start+plusCount] = flipStr(panCakeStrList[start:start+plusCount])
                    flipCount+=1
                else:
                   
                    panCakeStrList[start:end+1]=flipStr(panCakeStrList[start:end+1])
                    if not panCakeStrList[end]=='-':
                        end-=1
                    flipCount+=1
                
            else:
                
                if panCakeStrList[start:end]:
                    panCakeStrList[start:end]=flipStr(panCakeStrList[start:end])
                    flipCount+=1
                else:
                    
                    if panCakeStrList[end]=='-':
                        panCakeStrList[start:end+1] = flipStr(panCakeStrList[start:end+1])
                        flipCount+=1
                    end-=1
                
        else:            
            end-=1       
        
        if end<0:
            break
        counter+=1
        
        if validStr==''.join(panCakeStrList):
            break        
    
    fileOut.write('Case #{}: {}\n'.format(tcNo,flipCount))



def main():
    fileOut = open(r'D:\SpyderWorkspace\CodeJam\CodeJam16Results\B-large.out','w')
    fileIn = open(r'D:\SpyderWorkspace\CodeJam\CodeJam16Results\B-large.in','r')
    noOfTcs = int(fileIn.readline())   
    
    for tc in range(1,noOfTcs+1):
        inputStr = fileIn.readline()
        getOptimumFlips(tc,inputStr,fileOut)
    
    fileOut.flush()
    fileOut.close()
    fileIn.close()
#def main():
#    fileOut = open(r'D:\SpyderWorkspace\CodeJam\CodeJam16Results\B-small-attempt2.out','w')
#    fileIn = open(r'D:\SpyderWorkspace\CodeJam\CodeJam16Results\B-small-attempt2.in','r')
#    noOfTcs = int(fileIn.readline())   
#    
#   
#    getOptimumFlips(1,'++++--+',fileOut)
#    
#    fileOut.flush()
#    fileOut.close()
#    fileIn.close()


main()
    