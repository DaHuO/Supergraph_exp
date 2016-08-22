#! /usr/bin/env python3
# Written by Krzysio Leszczyński <chris@camk.edu.pl>
# Code Jam 2016

import sys

test_cases = int(sys.stdin.readline())

for test_case in range(1, test_cases+1):
    S = sys.stdin.readline().split()[0]
    lw = ""
    for c in S:
        lw = max(c+lw, lw+c)
    print("Case #{}: {}".format(test_case, lw))
        
