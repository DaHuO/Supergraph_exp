#!/usr/bin/env python
# -*- coding: utf-8 -*-


def solve(cipher):

    flips = 0
    current_run = None
    stack = list(cipher)

    for i in xrange(0, len(stack)):
        if i == len(stack)-1:
            if stack[i] == "-" and (current_run is not None and current_run != stack[i]):
                flips += 2
            elif current_run is not None and current_run != stack[i]:
                flips += 1
            elif stack[i] == "-":
                flips += 1
        elif i == 0:
            current_run = stack[i]
            continue
        elif stack[i] == current_run:
            continue
        else:
            current_run = stack[i]
            flips += 1
            continue
    return flips


if __name__ == "__main__":

    testcases = input()

    for caseNr in xrange(1, testcases+1):
        test_cast = raw_input()
        print("Case #%i: %s" % (caseNr, solve(test_cast)))
