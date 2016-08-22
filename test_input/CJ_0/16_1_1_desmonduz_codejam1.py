# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 02:02:00 2016

@author: Desmond
"""
import numpy as np

with open("A-large.in","r") as f:
    l=f.readlines()
    n=int(l[0])
    problems=list()
    for i in range(n):
        problems.append(l[i+1].strip()) 

output=""
for t, val in enumerate(problems):
    l=val[0]
    for i in range(1,len(val)):
        if val[i]<l[0]:
            l=l+val[i]
        else:
            l=val[i]+l
    output +="Case #%d: %s\n" % (t+1,l)
    print output

with open("output2.txt", "w") as f:
    f.write(output)