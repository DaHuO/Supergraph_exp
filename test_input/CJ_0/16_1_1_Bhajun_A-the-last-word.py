#!/usr/bin/env python

from __future__ import division, print_function
import sys


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for i in range(T):
        S = sys.stdin.readline().strip()
        X = S[0]
        
        for c in S[1:]:
            X = c + X if c >= X[0] else X + c
        
        print('Case #%d: %s' % (i + 1, X))