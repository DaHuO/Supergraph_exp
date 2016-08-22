#!/usr/bin/env python
# -*- coding: utf-8 -*-


def solve(cipher):
    front = [cipher[0]]
    back = []
    for c in cipher[1:]:
        if c >= front[len(front)-1]:
            front.append(c)
        else:
            back.append(c)

    front.reverse()
    front.extend(back)
    return ''.join(front)

if __name__ == "__main__":
    testcases = input()

    for case_num in xrange(1, testcases+1):
        cipher = raw_input()
        print("Case #%i: %s" % (case_num, solve(cipher)))
