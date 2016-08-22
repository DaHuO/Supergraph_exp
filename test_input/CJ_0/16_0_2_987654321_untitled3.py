# -*- coding: utf-8 -*-
"""
Created on Sat Apr 09 20:18:51 2016

@author: nick
"""

f = open('B-large.in', 'r')

def test_case(a):
    marker = a[0]
    flips = 0
    for i in range(len(a)):
        if a[i] != marker:
            flips = flips + 1
            marker =  a[i]
    
    #print str(flips) + "--> ",
    
    if marker == "-":
        flips = flips +1
    '''
    if flips > 0 and a[-1] == "+" and flips % 2 == 1:
        flips = flips -1 
    if flips > 0 and a[-1] == "-" and flips % 2 == 0:
        flips = flips +1 
    '''    
    return flips

case = 0
for line in f:
    if case != 0:
        print "Case #" + str(case) + ":",
        print test_case( line.rstrip() )
    case = case + 1