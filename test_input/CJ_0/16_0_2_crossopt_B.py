from sys import *

fin = open("b1.in", "r")
fout = open("b.out", "w")

t = int(fin.readline())
for i in range(1, t + 1):
    s = fin.readline().rstrip() + '+'
    n = len(s)
    print("Case #", i, ": ", end = '', sep = '', file = fout)
    ans = 0
    i = 0
    while i < n and s[i] == '-':
        i += 1
    if i != 0:
        ans += 1
    while i < n and s[i] == '+':
        i += 1
    while i < n:
        if s[i] == '+' and s[i - 1] == '-':
            ans += 2
        i += 1
    print(ans, file = fout)
        
fout.close()