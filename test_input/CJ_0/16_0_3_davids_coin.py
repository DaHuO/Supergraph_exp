from __future__ import print_function, division
import sys
from collections import defaultdict, Hashable
from functools import partial
from random import shuffle, choice
import heapq
from itertools import izip,groupby,product
from math import sqrt

#from primesieve.numpy import *
#import primesieve

def read_case(f):
    n, j = map(int, f.readline().split(' '))
    return (n,j)

in_ = open(sys.argv[1], 'r')
num_cases = int(in_.readline())
cases = [read_case(in_) for n in range(num_cases)]
#cases = [(6, 300)] # test
#cases = [(16, 50)] # small
#cases = [(32, 500)] # large
#cases = [''.join([choice('-+') for i in range(100)]) for j in range(200)]
n, j = cases[0]

divisors = defaultdict()

def divisor(n):
    if n in divisors:
        return divisors[n]
    i = 2
    while i*i < n+1:
        if n % i == 0:
            divisors[n] = i
            return i
        i+= 1
        if i >=10**5:
            break
    divisors[n] = None
    return None


def print_case(result, n, f):
    text = "Case #%d:\n" % (n)
    for j, divs in result:
        text += str(j) + ' ' + ' '.join(map(str,divs)) + '\n'
    out.write(text )#+ '\n')
    print(text)
    
factors = [[base**exp for exp in range(n-1,-1,-1)] for base in range(0,10+1)]

def do_case(case):
    coins = []
    for digits in product([0,1], repeat=n-2):
        if len(coins) >= j:
            break
        good = True
        divisors = [0]*11
        digits = [1]+list(digits)+[1]
        for base in range(2,10+1):
            t = 0
            for i,digit in enumerate(digits):
                t += digit * factors[base][i]
            #t = int(''.join(map(str, digits)), base)
            #print(''.join(map(str,digits)), ' t:', t)
            divisors[base] = divisor(t)
            if divisors[base] is None:
                #print(''.join(map(str,digits)), 'base:', base, ' ', t, 'prime')
                good = False
                break
        if good:
            print(''.join(map(str,digits)),divisors[2:])
            coins.append((''.join(map(str,digits)),divisors[2:]))
    print('num coins:', len(coins))
    res = coins
    return res
    


results = [do_case(case) for case in cases]

out = open(sys.argv[2], 'w')
for n,result in enumerate(results):
    print_case(result, n+1, out)
