#! /usr/bin/python

import sys
import math

if len(sys.argv) < 2:
	exit(1)

finname = sys.argv[1]
foutname = finname.replace(".in",".out")

print "{} {}".format(finname,foutname)

fin=open(finname,"r")
fout=open(foutname,"w")

numcases=int(fin.readline());

print numcases

def createNum (numStr, base):
    retNum=0;
    for i in range(0,len(numStr)):
        if '1' == numStr[i]:
            #print "retNum before: %d, base: %d, i: %d" % (retNum,base,len(numStr)-1-i)
            retNum+=math.pow(base, len(numStr)-1-i)
            #print "retNum after : %d" %retNum
    return retNum

def findDivisor (num):
    sqrt=int(math.sqrt(num))+1
    i=2
    while i < sqrt:
        if 0 == num%i:
            return i
        i=i+1
    return 0

for case in range(0,numcases):
    fout.write ("Case #%d:\n" % (case+1))
    line=fin.readline().strip()
    line=line.split()

    n=int(line.pop(0))
    j=int(line.pop(0))

    baseStr=""
    for i in range(0,n):
        baseStr+="0"
    baseStr=list(baseStr)
    baseStr[0]='1'
    baseStr[n-1]='1'
    baseStr="".join(baseStr)
   
    print "str: %s" % baseStr
    
    base=int(baseStr,2)
    
    first=True
    
    found=0

    while found!=j:
        if False==first:
            base+=2;
        else:
            first=False
        baseStr="{0:b}".format(base)

        print "base_str: %s" % baseStr

        divisorStr=""
        for i in range(2,11):

            num=createNum(baseStr,i)
            divisor=findDivisor(num)
            divisorStr+="%d " % divisor
            if divisor>0:
                divident=num/divisor
                print "divisor for num:%d base %d: %d, divident %d, check: %d" % (num,i,divisor, divident, divident*divisor)
            if 0==divisor:
                print "OOPS :("
                break
            if 10==i:
                found=found+1
                print "HEUREKA #%d" % found
                fout.write("%s %s\n" % (baseStr,divisorStr))

        
#    line=fin.readline().strip()
#    line=line.split()

#    k=int(line.pop(0))
#    c=int(line.pop(0))
#    s=int(line.pop(0))

#    print "k: %d,c: %d, s: %d, half: %d" % (k,c,s,(k+k%2)/2)
#    actnum=0
#    count=0
#    level2_size=k*k;
    
#    if 1==c:
#        if s<k:
#            fout.write("IMPOSSIBLE")
#        else:
#            for i in range(0,s):
#                fout.write("%d " % (i+1))
#    else:
#        if s<(k+k%2)/2:
#            fout.write("IMPOSSIBLE")
#        else:
#            for i in range(0,(k+k%2)/2):
#                tile=2*i*k+2*i+1
#                if tile==k*k:
#                    tile=tile-1
#                fout.write("%d " % (tile+1))
#    fout.write("\n");
    
    #while False==truearr (numList):
    #        count+=1
    #        actnum+=num
    #        numstr=str(actnum)
    #        print "numstr: %s" % numstr
    #        for i in range(0,len(numstr)):
    #            numList[int(numstr[i])]=True
    #fout.write("%d\n" % actnum)
    #print "count: %d" % (count)


#    print "r: %d, w: %d, c: %d" % (r,w,c)

#    if (c == w):
#        print "sol: %d" % (w)
#        sol=w
#    else:
#        div=int(c/w)
#        if(0 == c%w):
#            div=div-1
#        sol=div+w
#        print "sol: %d" % (sol)
#    fout.write ("%d\n" % (sol))

#	print "%d %d" % (sum1, sum2)
#	fout.write("%d %d\n" % (sum1, sum2) )
			



