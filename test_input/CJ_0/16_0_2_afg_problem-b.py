#!/usr/bin/env python3

def flips_needed(stack):
    flips = 0
    for i in range(len(stack) - 1):
        if stack[i] != stack[i + 1]:
            flips += 1
    if stack[-1] == '-':
        flips += 1
    return flips

for case_number in range(int(input())):
    print('Case #{}: {}'.format(case_number + 1, flips_needed(input())))
