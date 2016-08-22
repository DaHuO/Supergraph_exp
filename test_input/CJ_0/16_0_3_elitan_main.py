#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from baseconv import BaseConverter
from math import sqrt
from time import sleep

def get_prime_factor(n):
    nR = n
    i = 3
    arr = []

    while i < sqrt(n) + 1:
        while n % i == 0:
            return i
            #arr.append(i)
            #n = n / i

        i += 2

    if n != nR:
        return n


    return False


def find_prime(f, base, res):
    conv = BaseConverter(('').join(map(str, [ tmp for tmp in range(0, base) ])))
    f = int(conv.decode(f))
    if base == 10:
        factor = get_prime_factor(f)
        if factor:
            res.append(factor)
            return True
        else:
            return False

    factor = get_prime_factor(f)
    if factor:
        res.append(factor)
        return find_prime(conv.encode(f), base+1, res)
    else:
        return False

def main():
    for t in range(int(input())):

        print('Case #%d:' % (t + 1))
        n, j = map(int, input().split(' '))
        #print(('').join(map(str, [ tmp for tmp in range(0, x) ])))
        #conv = BaseConverter(('').join(map(str, [ tmp for tmp in range(0, x) ])))
        #s = ('%s1' % (('').join(map(str, [0 for tmp in range(0, n-2)]))))
        b2 = BaseConverter('01')
        f = b2.encode(pow(2, n-1) + 1)
        f = pow(2, n-1) + 1
        
        found = 0
        while found < j:
            res = []
            if find_prime(b2.encode(f), 2, res):
                print('%s %d %d %d %d %d %d %d %d %d' % (b2.encode(f), res[0], res[1], res[2], res[3], res[4], res[5], res[6], res[7], res[8]))
                found += 1
            f += 2


if __name__ == "__main__":
    main()
