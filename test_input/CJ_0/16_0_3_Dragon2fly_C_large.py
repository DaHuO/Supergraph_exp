#!/usr/bin/env python 
# -*- coding: utf-8 -*-
__author__ = 'duc_tin'

from math import sqrt
from subprocess import Popen, PIPE
from itertools import product


def fermat(n):
    if n == 2:
        return True
    if not n & 1:
        return False
    return pow(2, n - 1, n) == 1


def next_prime(n):
    if fermat(n):
        n += 1
    if (n % 2 == 0) and (n != 2):
        n += 1
    while True:
        if fermat(n):
            break
        n += 2
    return n


def get_divisor(num):
    with open('testgp.gp', 'w+') as gpfile:
        content = "print(factor(%s))\nquit" % num
        gpfile.write(content)

    cmd = ['gp', '-q', 'testgp.gp']
    res = Popen(cmd, stdout=PIPE, stderr=PIPE, bufsize=1).communicate()[0]
    return res[1:-2].split(';')[0].split(',')[0]

# =====================================================

T = int(raw_input())

for case in range(1, T + 1):
    N, J = map(int, raw_input().strip().split())
    j = 0
    print "Case #1:"

    for coin in product('01', repeat=N - 2):
        if j == J: break
        jamcoin = '1' + ''.join(coin) + '1'
        all_base = []

        # print jamcoin

        for n in range(2, 11):
            num = int(jamcoin, n)
            all_base.append(num)
            if fermat(num):
                all_base = []
                break

        if not all_base:
            continue

        else:
            j += 1
            divides = []
            for nu in all_base:
                divides.append(str(get_divisor(nu)))
            print jamcoin, ' '.join(divides)
