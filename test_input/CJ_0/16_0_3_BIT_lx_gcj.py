# -*- coding: utf-8 -*-

import random, math
from itertools import count

N = 32
J = 500
vis = []
LIM = 10000000
f = open('c.out', 'w')

prime = []
mark = {'0': 0, '1': 0}
for i in count(2):
    if i >= LIM: break
    if (not (str(i) in mark)): prime.append(i)
    for j in range(0, len(prime)):
        if i * prime[j] > LIM: break
        mark[str(i * prime[j])] = 0
        if (i % prime[j] == 0): break
print('make prime done!')

def getNumStr():
    global vis
    global N
    while True:
        str = '1' + ''.join([random.choice(['0', '1']) for _ in range(N - 2)]) + '1'
        if not (str in vis):
            vis.append(str)
            return str


def ok(ss):
    pp = []
    for bb in range(2, 11):
        num = int(ss, bb)
        flag = False
        for x in prime:
            if x * x > num: break
            if num % x == 0:
                flag = True
                pp.append(str(x))
                break
        if not flag: return None
    return pp


f.write('Case #1:\n')
for i in range(J):
    while True:
        ss = getNumStr()
        pp = ok(ss)
        if pp is not None:
            f.write(ss + ' ')
            f.write(' '.join(pp))
            f.write('\n')
            break
    if i % 50 == 0:
        print("%d done!" % i)
f.close()
