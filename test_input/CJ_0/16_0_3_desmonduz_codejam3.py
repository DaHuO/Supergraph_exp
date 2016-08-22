# -*- coding: utf-8 -*-
"""
Created on Sat Apr 09 22:22:42 2016

@author: Desmond
"""
#from __future__ import division
#import numpy as np
#import itertools
#import math
#
#with open("C-small-attempt0.in","r") as f:
#    l=f.readlines()
#    n=int(l[0])
#    problems=list()
#    for i in range(1,n+1):
#        parts=l[i].split()
#        problems.append([int(parts[0]), int(parts[1])])
#
#def getNumBase(binstr, base):
#    return sum([int(s)*base**i for i,s in enumerate(binstr)])
#
#def getDivisor(num):
#    for i in range(2,int(math.floor(math.sqrt(num)))):
#        if (num % i == 0): return i
#    return None
#
#output=""
#for t,p in enumerate(problems):
#    sols=list()
#    for posval in itertools.product([0,1],repeat=p[0]-2):
#        if sum(posval) % 2==0:
#            v="1%s1" % "".join(str(s) for s in posval)
#            divs=list()
#            for i in range(2, 11):
#                x=getNumBase(v, i)
#                if i % 2==0:
#                    y=getDivisor(x)
#                    if y: divs.append(y)
#                else:
#                    divs.append(2)
#            if len(divs)==9:
#                sols.append("%s %s" % (v, " ".join(str(d) for d in divs)))
#                print sols[-1]
#            if len(sols)==p[1]:
#                break
#        
#    print sols
#    output +="Case #%d:\n" % (t+1)
#    output += "\n".join(sols)
#
#print output
#with open("output2.txt", "w") as f:
#    f.write(output)

#checker
for sol in sols:
    vals=sol.split(" ")
    for i,b in enumerate(range(2,11)):
        if (getNumBase(vals[0],b) % int(vals[i+1]) !=0): print "Fuck you! %s %s %s" % (vals[0], b, vals[i+1])

