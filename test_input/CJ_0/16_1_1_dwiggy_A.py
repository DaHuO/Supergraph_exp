#!/usr/bin/python

import sys

T = int(sys.stdin.readline())

for i in range(0,T):
    cases = sys.stdin.readline().strip()
    last_word = []
    last_word.append(cases[0])
    cases = cases[1:]
    for c in cases:
        if (c >= last_word[0]):
            last_word = [c, ] + last_word
        else:
            last_word.append(c)
    print ("Case #"+str(i+1)+": "+"".join(last_word))
