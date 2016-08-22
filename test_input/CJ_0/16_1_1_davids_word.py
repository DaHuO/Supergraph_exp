from __future__ import print_function, division
import sys
from collections import defaultdict, Hashable
from functools import partial
from random import shuffle, choice
import heapq
from itertools import izip,groupby,product
from math import sqrt

def read_case(f):
    c = f.readline().rstrip()
    return c

in_ = open(sys.argv[1], 'r')
num_cases = int(in_.readline())
cases = [read_case(in_) for n in range(num_cases)]
#cases = [(6, 300)] # test
#cases = [(16, 50)] # small
#cases = [(32, 500)] # large
#cases = [''.join([choice('-+') for i in range(100)]) for j in range(200)]


def print_case(result, n, f):
    text = "Case #%d: %s" % (n, result)
    out.write(text + '\n')
    print(text)
 

def do_case(case):
    chars = case
    cur = chars[0]
    for c in chars[1:]:
        if c >= cur[0]:
            cur = c + cur
        else:
            cur = cur + c

    return cur
    


results = [do_case(case) for case in cases]

out = open(sys.argv[2], 'w')
for n,result in enumerate(results):
    print_case(result, n+1, out)
