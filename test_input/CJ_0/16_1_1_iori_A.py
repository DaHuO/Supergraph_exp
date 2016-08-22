#!/usr/bin/env python3

T = int(input())
for t in range(1, T+1):
    ans = ''
    s = input()
    ans = s[0]
    for i in s[1:]:
        if ans[0] > i:
            ans += i
        else:
            ans = i + ans
    print("Case #{}: {}".format(t, ans))
