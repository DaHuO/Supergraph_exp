#!/usr/bin/env python3

def solve(pancakes):
    curr = pancakes[-1]
    num = 0 if curr == '+' else 1
    for p in reversed(pancakes[:-1]):
        if p != curr:
            num += 1
            curr = p
    return num

if __name__ == '__main__':
    for idx in range(1, int(input()) + 1):
        pancakes = input()
        print("Case #{}: {}".format(idx, solve(pancakes)))
