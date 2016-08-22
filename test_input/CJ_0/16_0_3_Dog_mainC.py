#! /usr/bin/env python3

import re
import random as rnd

rnd.seed(1)

def enumerate_coins(N):
    for i in range(2**(N - 2)):
        s = '1{:0{}b}1'.format(i, N-2)
        yield [int(x) for x in s]

def random_enumerate_coins(N):
    m = 2 ** (N-2)
    done = set()
    while True:
        i = rnd.randint(0, m)
        s = '1{:0{}b}1'.format(i, N-2)
        if s in done: continue
        done.add(s)
        yield [int(x) for x in s]

class Solver(object):

    def __init__(self, N):
        self.N = N
        self.bases = dict()
        for b in range(2, 11):
            self.bases[b] = [b**i for  i in range(N-1, -1, -1)]

    def test_coin(self, coin):
        self.divs = list()
        for b in range(2, 11):
            d = self._test_coin(coin, b)
            if d is None: return None
            self.divs.append(d)
        return list(self.divs)

    def _test_coin(self, coin, b):
        rep = sum(i*bb for (i, bb) in zip(coin, self.bases[b]))
        for i in range(3, min(10000, rep)):
            if i in self.divs: continue
            if rep % i == 0: return i
        return None

import sys
with open(sys.argv[1]) as f:
    content = f.read()

ns = re.findall(r'\d+', content)
N = int(ns[1])
J = int(ns[2])
s = Solver(N)
i = 0
print('Case #1:')
#for coin in enumerate_coins(N):
for coin in random_enumerate_coins(N):
    strcoin = ''.join(map(str, coin))
    divs = s.test_coin(coin)
    if divs is None: continue
    i += 1
    if i > J: break
    strdivs = ' '.join(map(str, divs))
    print(strcoin, strdivs)
