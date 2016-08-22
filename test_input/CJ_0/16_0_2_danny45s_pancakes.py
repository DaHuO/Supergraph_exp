import numpy as np
import sys
a=open(sys.argv[-1]).readlines()[1:]


def solve(pancakes):
    num = 0
    if pancakes[0] == '-':
        num += 1
    for i in range(len(pancakes) - 1):
        if pancakes[i] == '+' and pancakes[i + 1] == '-':
            num += 2
    return num

for i in range(len(a)):
    print 'Case #' + str(i + 1) + ': ' + str(solve(a[i]))
