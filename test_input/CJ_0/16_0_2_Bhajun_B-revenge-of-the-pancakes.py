#!/usr/bin/env python

from __future__ import division, print_function
import sys


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for i in range(T):
        S = sys.stdin.readline().strip()
        X = [c == '+' for c in S]
        
        count = 0
        
        for j in reversed(range(len(X))):
            if not X[j]:
                # Count and flip the happy pancakes on top
                top_happy = 0
            
                while X[top_happy]:
                    X[top_happy] = False
                    top_happy += 1

                if top_happy > 0:
                    count += 1
                
                # Flip the pancake stack until the last unhappy pancakes
                for k in range(j + 1):
                    X[k] = not X[k]
                    
                for k in range((j + 1) // 2):
                    X[k], X[j - k] = X[j - k], X[k]
                
                count += 1
        
        print('Case #%d: %d' % (i + 1, count))