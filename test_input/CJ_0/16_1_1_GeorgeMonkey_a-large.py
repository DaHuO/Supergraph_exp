#!/bin/env python
from __future__ import print_function
import sys
import os
import os.path

fi = open(sys.argv[1], 'r')
fo = open(os.path.splitext(sys.argv[1])[0] + '.large.out', 'w')

T = int(fi.readline().strip())
for k in range(T):
    s = fi.readline().strip()
    ret = ''
    for c in s:
        if len(ret) == 0 or c >= ret[0]:
            ret = c + ret
        else:
            ret = ret + c
    print('Case #%d:' % (k + 1), ret, file=fo)

fi.close()
fo.close()
