# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 01:52:36 2016

@author: Emad Yehya
"""

import math

N = 16
J = 50


L = ["0", "1"]

for i in range(0, N-3):
    L2 = []
    for k in L:
        L2.append(k + "0")
        L2.append(k + "1")
    L = L2

L2 = []
for k in L:
    L2.append("1" + k + "1")
    
ans = []
proof = []
curr_proof = []

def confirm_nonprimality(n):
    if(n%2 == 0):
        curr_proof.append(2)
        return True
    else:
        for i in range(3, int(math.sqrt(n))+1, 2):
            if(n%i == 0):
                curr_proof.append(i)
                return True
        return False

for k in L2:
    print "Found " + str(len(ans))
    if(len(ans) >= J):
        break
    composite = True
    for b in range(2, 11):
        if(not composite):
            break
        composite = confirm_nonprimality(int(k, b))
    if(composite):
        ans.append(k)
        proof.append(curr_proof)
    curr_proof = []
        
print "Case #1:"
for i in range(0, J):
    print ans[i], proof[i][0], proof[i][1], proof[i][2], proof[i][3], proof[i][4], proof[i][5], proof[i][6], proof[i][7], proof[i][8]