# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 16:36:24 2016

@author: dagoth
"""

import numpy as np
import decimal

def bin_to_dig(s, base):
   res = 0
   for i in range(len(s)):
       res = res * base
       if s[i] == '1':
           res = res + 1
   return res 

def dig_to_bin(dig):
    s = ''
    while (dig > 0):
        if dig & 1:
            s = s + '1'
        else:
            s = s + '0'
        dig = dig >> 1
    s = s[::-1]
    return s
    
def is_prime(dig):
    end = min(dig, 1000)
    if dig % 2 == 0:
        return 2
    for i in range(3, end, 2):
        if dig % i == 0:
            return i
    return -1

#%%   

f = open('/home/dagoth/C.in', 'r')

T = f.readline()
Vals = f.readline()
Vals = Vals.split()
N = int(Vals[0])
J = int(Vals[1])


beg = 2 ** (N - 1) + 1
results = []
divs = [[] for i in range(J)]
z = 0
#%%
for q in range(beg, beg + 100000, 2):
    print(z)
    if z >= J:
        break
    bv = dig_to_bin(q)
    divisors = []
    o = 1
    
    for base in range(2, 11):
        dig = bin_to_dig(bv, base)
        num = is_prime(dig)
        
        if num != -1:
            divisors.append(num)
        else:
            o = 0
            break
        
    if o == 1:
        results.append(bv)
        divs[z] = divisors
        z = z + 1
        
    del divisors
    del bv
#%%
ss = [0] * J
    
for i in range(len(divs)):
    ss[i] = results[i] + ' '
    for item in divs[i]:
        ss[i] = ss[i] + str(item) + ' '
#%%
f_w = open('/home/dagoth/C.out', 'w')
f_w.write('Case #1:\n')

for i in range(len(ss)):
    f_w.write(ss[i] + '\n')
