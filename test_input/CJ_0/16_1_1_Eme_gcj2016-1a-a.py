#!/usr/bin/env python3
def solve(s, i, cur):
    if i == len(s):
        return cur
    else:
        a = solve(s, i + 1, cur + s[i])
        b = solve(s, i + 1, s[i] + cur)
        return max(a, b)

if __name__ == '__main__':
    num_cases = int(input())
    for c in range(1, num_cases + 1):
        s = input()
        print("Case #{}: {}".format(c, solve(s, 0, "")))
