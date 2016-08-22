#!/usr/bin/python3

import sys

MAXDIV=100

T = int(sys.stdin.readline().strip())
l = sys.stdin.readline().strip().split(' ')
N = int(l[0])
J = int(l[1])
print("Case #1:")

def inttobase(i, b):
    if i == 0:
        return "0"
    s = ""
    while i > 0:
        s += str(i % b)
        i /= b
    return s

def tobin(s):
    return "{0:b}".format(current)

def intasbase(s, b):
    v = 0
    for i in range(len(s)):
        v *= b
        v += int(s[i])
    return v

def isjam(v):
    l = []
    for b in range(2,11):
        v = intasbase(tobin(v), b)
        ok = False
        for j in range(2, min(MAXDIV, v-1)):
            if v % j == 0:
                l.append(j)
                ok = True
                break
        if not ok:
            return []
    return l

current = 2**(N-1)+1
while J > 0:
    l = isjam(current)
    if len(l) > 0:
        print(tobin(current) + " " + " ".join(str(x) for x in l))
        J -= 1
    current += 2




