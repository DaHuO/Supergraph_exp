import sys
import string
import re

T = int(input())

for i in range(1, T + 1):
    s = input()

    s = re.sub("\++", "+", s)
    s = re.sub("-+", "-", s)

    if '-' not in s:
        print("Case #{}: 0".format(i))
        continue

    if '+' not in s:
        print("Case #{}: 1".format(i))
        continue

    cost = 0
    skipNext = False
    for j in range(0, len(s) - 1):
        if skipNext or s[j+1] == s[j]:
            skipNext = False
            continue
        elif s[j+1] == '+':
            cost += 1
        else:
            cost += 2
            skipNext = True

    print("Case #{}: {}".format(i, cost))
