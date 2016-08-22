#! /usr/bin/env python3
# Written by Krzysio Leszczyński <chris@camk.edu.pl>
# Code Jam 2016

import sys

def flipped(pcake):
    return [ not v for v in reversed(pcake) ]

# pcake represent +-+-----+----------------
def pancake_flips(pcake):
    N = 0
    while len(pcake):
        if pcake[-1]:
            pcake = pcake[:-1]
            continue
        assert not pcake[-1]
        # Find the longest ++++ at the begin
        if pcake[0]:
            for k in range(1,10000):
                if not pcake[k]:
                    pcake = flipped(pcake[:k]) + pcake[k:]
                    N += 1
                    break
        assert not pcake[0]
        pcake = flipped(pcake)
        N += 1
    return N
    

test_cases = int(sys.stdin.readline())

plusminus = { '-': False, '+': True }

for tcase in range(1, test_cases+1):
    
    print("Case #{}: {}".format(
        tcase,
        pancake_flips(
            [ plusminus[c] 
              for c in sys.stdin.readline().split()[0] ])))

