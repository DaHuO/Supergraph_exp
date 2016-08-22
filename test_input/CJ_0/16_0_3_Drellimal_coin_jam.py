# -*- coding: utf-8 -*-
"""
Created on Fri Apr 08 21:27:24 2016

@author: Dane
"""
import math
def prime(n, step):
    step = 2 - (step % 2)
    for x in range(3, int(math.sqrt(n)+0.5), step):
        if n % x  == 0:
            return [x, n/x]
    return [-1,-1]

def find_stuff(n):
    factors= []
    for x in range(2,11):
        a = prime(int(n,x),x)
        if  a == [-1,-1]:
            return []
        else:
            if x % 2 == 0:
                factors += [str(a[0])]
            else:
                factors += [str(a[1])]
    return factors

for y in range(int(raw_input())):
    N, J = [int(x) for x in raw_input().split()]
    valid =[]
    print "Case #{}:".format(y+1)
    while len(valid) < J:
        for x in range(2**(N-1) +1, 2**N -1, 2):
            if len(valid) >= J:
                break
            a = bin(x)[2:]
            afac = find_stuff(a)
            if len(afac) >0:
                valid += [a]
                print "{} {}".format(a, " ".join(afac))
                
                
    
            
        
