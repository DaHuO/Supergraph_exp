#!/usr/bin/python

import sys

index = 1
num = input()
for line in sys.stdin.readlines():
    print("Case #" + str(index), end=': ')
    index+=1

    # recursively make the string
    # make the last letter of S first.
    # ACDFGZ BBBBBBBB
    # if incoming letter is larger than my first letter, put it there.

    outstr = ''
    for c in line:
        if len(outstr) == 0:
            outstr += c
        elif c >= outstr[0]:
            outstr = c + outstr
        else:
            outstr += c

    print(outstr, end="")
