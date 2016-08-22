#!/usr/bin/env python3

T = int(input())

for t in range(1, T + 1):
    s = input()
    
    while '++' in s:
        s = s.replace('++', '+')
    while '--' in s:
        s = s.replace('--', '-')

    if s[-1] == '+':
        s = s[:-1]

    print("Case #{}: {}".format(t, len(s)))
