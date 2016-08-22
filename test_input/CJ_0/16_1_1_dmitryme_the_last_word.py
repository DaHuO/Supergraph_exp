#!/usr/bin/python
import sys

fl = open(sys.argv[1])

cases = int(fl.readline())

for case_number in range(1, cases + 1):
    line = fl.readline().strip()

    result = ''
    for ch in line:
        if ch + result > result + ch:
            result = ch + result
        else:
            result = result + ch

    print 'Case #%s: %s' % (case_number, result)
