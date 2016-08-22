# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

fout = open('A-large.out', 'w')
with open('A-large.in') as f:
    T = int(f.readline())
    for case in range(T):
        S = f.readline().strip()
        lastWord = S[0]
        for c in S[1:]:
            if c < lastWord[0]:
                lastWord += c
            else:
                lastWord = c + lastWord
        print('Case #'+str(case+1)+': '+lastWord, file=fout)
fout.close()