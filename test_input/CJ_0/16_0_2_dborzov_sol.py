#!/usr/bin/env python

# A.py


from __future__ import print_function
import sys


input_data = open(sys.argv[1])
filename, _ = sys.argv[1].split(".")
output_data = open(filename + ".out","w")

num_tests = int(input_data.readline().rstrip())
for i in range(1,num_tests+1):
    line = input_data.readline().rstrip()
    N=1
    cur_sign = line[0]
    # import pdb; pdb.set_trace()
    for ss in line:
        if ss != cur_sign:
            cur_sign = ss
            N +=1
    if cur_sign == '+':
        N = N-1
    output_data.write("Case #%s: %s\n" % (i, N))
