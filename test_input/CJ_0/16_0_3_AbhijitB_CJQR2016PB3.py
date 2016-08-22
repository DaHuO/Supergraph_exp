# -*- coding: utf-8 -*-
"""
Created on Sat Apr 09 14:28:47 2016

@author: abhibhat
"""
from sympy import primetest, primefactors
from itertools import count
def CJQR2016PB3(N, J):
    def div(N):
        return not any(primetest.isprime(int(N, b)) for b in range(2, 11))
    def factor(N):
        return [str(primefactors(int(N, b))[0]) for b in range(2, 11)]
    N -= 2
    num = 1+(1 << (N+1))
    for i in count(1931264):
        if J == 0: return
        jamcoin = "{:b}".format(num +( i << 1))
        if div(jamcoin):
            yield "{} {}".format(jamcoin, ' '.join(factor(jamcoin)))
            J -= 1
print "Case #1:"            
for result in CJQR2016PB3(32, 500):
    print result