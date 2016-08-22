# -*- coding: utf-8 -*-
"""
Created on Sat Apr 09 09:53:38 2016

@author: abhibhat
"""

def CJQR2016PB2(pan):
    sides = {"+":"-", "-":"+"}
    count = 0
    try:
        while True:
            index = pan.index(sides[pan[0]])
            pan[:index] = sides[pan[0]] * index
            count += 1
    except ValueError:
        return count + int(pan[0] == '-')
    
T = input()
for i in range(1, T + 1):
    pan = list(raw_input())
    print "Case #{}: {}".format(i, CJQR2016PB2(pan))