#! /usr/bin/env python

import math
import itertools

#  +---+---+---+
#  | a | b | c |
#  +---+---+---+
#  0   1   2   3
# -3  -2  -1

def flip(c):
    if c == '-': 
        return '+'
    elif c == '+': 
        return '-'

def plus(c): 
    return c == '+'
def minus(c):
    return c == '-'
        
if __name__ == "__main__":
    T = int( input() )
    
    for x in range(1,T+1):
        
        P = list(input())
        
        f = 0   # number of flips
        
    
        phase = 0
        L = 0   # left bound
        R = len(P) - 1  # right bound
        # search for plus from right
        while 0 <= R and plus(P[R]):
            R = R - 1
        
        while L <= R:
            i = L   # left pointer
            j = R  # right pointer
            if phase == 0: # plus from right and jump for minus from left
                # jump cluster of plus and search for minus from left
                k = 0
                while i <= R and plus(P[i]):   # jump cluster of plus
                    i = i + 1
                    k = k + 1
                while i <= R and minus(P[i]):  # search for minus
                    i = i + 1
                if k > 0 and k+L < i:
                    f = f + 1   # flip all plus on the left
                f = f + 1   # flip the top of the pile
                phase = 1   # change phase
                L = i   # move left boundary
                # search for minus from left
                while L <= R and minus(P[L]):
                    L = L + 1
                R = j   # move right boundary
            else:   # jump for plus from right and minus from left
                # jump cluster of minus and search for plus from right
                k = 0
                while L <= j and minus(P[j]):
                    j = j - 1
                    k = k + 1
                while L <= j and plus(P[j]):
                    j = j - 1
                if k > 0 and j < R-k:
                    f = f + 1   # flip all minus on the right
                f = f + 1   # flip the top of the pile
                phase = 0   #change phase
                L = i   # move left boundary
                R = j   # move right boundary
                # search for plus from right
                while 0 <= R and plus(P[R]):
                    R = R - 1
        
        print('Case #%i: %i' % (x,f))
