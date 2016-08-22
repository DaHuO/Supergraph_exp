#!/usr/bin/env python
import sys


def solve_case(input_str):
    current = input_str[:1]
    for i in input_str[1:]:
        if i >= current[0]:
            current = i + current
        else:
            current = current + i
    return current

def read_and_solve():
    case_num = int(sys.stdin.readline())
    for i in xrange(1, case_num + 1):
        solution = solve_case(sys.stdin.readline().strip())
        print 'Case #{}: {}'.format(i, solution)


if __name__ == '__main__':
    read_and_solve()
