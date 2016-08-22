# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 03:48:06 2016

@author: rajbhagat
"""
def flip(listinside):
    k=[]
    for everything in listinside:
        
        if everything=='-':
            k.append('+')
        else:
            k.append('-')
    return k
 
fileopen = open("C:/Users/rajbhagat/Downloads/B-large.in",'r')
writefile=open("C:/Users/rajbhagat/Downloads/B-large.out",'w')
i=0


for content in fileopen:
    if i>0:
        initlist=list(content.rstrip())
        initlen=len(initlist)
        count=0
        j=-1
        t=0
        s=0
        finallist=[]
        finallist[:]=initlist[:]
        while t<len(initlist):
            actlen=initlen+j+1
            if finallist[j]!='+':
                finallist[:actlen]=flip(finallist[:actlen])
                count+=1
            j-=1
            t+=1
        
        
        print count            
        writefile.write("Case #"+str(i)+": "+str(count))
        writefile.write("\n")
        
    i+=1
writefile.close()