#!/usr/bin/env python3

def calc(s, n, c):
    if n == 1:
        return 0 if s[0] == c else 1
    if s[n-1] == c:
        return calc(s, n-1, c)
    return calc(s, n-1, s[n-1]) + 1

T = int(input())
for t in range(T):
    s = input()
    r = calc(s, len(s), '+')
    print("Case #{}: {}".format(t + 1, r))
