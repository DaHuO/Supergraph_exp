#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import math
import time


def compute(word):
    result = [word[0]]
    for i in range(1, len(word)):
        alpha = word[i]
        if alpha >= result[0]:
            result.insert(0, alpha)
        else:
            result.append(alpha)
    return ''.join(result)


if __name__ == "__main__":
    with open(sys.argv[1], 'r') as f:
        cases = int(f.readline())
        for i in range(cases):
            word = f.readline().strip()
            result = compute(word)
            print('Case #{}: {}'.format(i+1, result))
