#!/usr/bin/env python
# -*- coding: utf-8 -*-


def solve_neg_pos(s):
    if s == '-':
        return 0, 1
    elif s == '+':
        return 1, 0
    else:
        n, p = solve_neg_pos(s[:-1])
        last_char = s[len(s)-1]
        if last_char == '-':
            return n, n+1
        else:
            return p+1, p


def solve(cipher):
    return solve_neg_pos(cipher)[1]

if __name__ == "__main__":
    testcases = input()

    for case_num in xrange(1, testcases+1):
        cipher = raw_input()
        print("Case #%i: %s" % (case_num, solve(cipher)))
