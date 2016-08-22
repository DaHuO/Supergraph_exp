#!/usr/bin/env python

inFile="B-large.in"
cases=[]
with open(inFile) as f:
    content=f.readlines()
    caseNum=int(content[0].strip('\n'))
    for en in range(caseNum):
        oneCase=content[en+1].strip('\n')
        cases.append(oneCase)
f.close()
typemap={'+':'-','-':'+'}
for en in range(len(cases)):
    bfp=[]
    cnt=0
    for p in range(len(cases[en])):
        pancake=cases[en][p]
        setType=pancake
        bfp.append(pancake)
        if len(set(bfp))>1:
            if pancake!=cases[en][p-1]:
                cnt=cnt+1
            
    if setType=='-':
        cnt=cnt+1
                
    print "Case #"+str(en+1)+": "+str(cnt)