#!/usr/bin/env python3
import itertools

def odds(i):
    return [i*2+1 for i in range(i//2-1)]
def evens(i):
    return [i*2+2 for i in range(i//2-1)]

with open('primes.txt') as p:
    primes = [int(i) for i in p.read().split()]

def num(pows, n):
    return sum(n**i for i in pows)

def composite(num):
    for i in primes:
        if i >= num:
            return 0
        if num % i == 0:
            return i
    return 0

A = 32
B = 500
Q = (2, 5)
S = [i for i in range(1, A+2) if i % 6 == 0]

def getcombos():
    n = 0
    dat = []
    for q in Q:
        for i in itertools.combinations(odds(A), q):
            for j in itertools.combinations(evens(A), q):
                pows = i + j + (0, A-1)
                d = ['0'] * A
                for p in pows:
                    d[p] = '1'
                sn = ''.join(d)
                cs = composite(int(sn, 6))
                if cs:
                    dat.append((sn, cs))
                    n += 1
                    if n >= B:
                        return dat

def processcombo(c):
    sn, sixdivisor = c
    divisors = [3, 2, 3, 2, sixdivisor, 2, 3, 2, 3]
    ns = [i+2 for i in range(9)]
    for n, d in zip(ns, divisors):
        if int(sn, n) % d != 0:
            print("FUCK ", sn, n)
    return sn, divisors

print("Case #1:")
for sn, divisors in map(processcombo, getcombos()):
    print(sn + ' ' + ' '.join(str(i) for i in divisors))

