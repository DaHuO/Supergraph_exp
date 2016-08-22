#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import numpy as np

primelist=np.load(open("primer", "rb"))
primelist_size=len(primelist)

def is_prime(num) :
    index = np.searchsorted(primelist, num)
    if index >= primelist_size :
        return False
    return primelist[index] == num

def found_divide(num) :
    for i in primelist :
        if num%i == 0 :
            return i
    return None

def jamcoin_to_int(jamcoin, base) :
    convert=0
    current=1

    for bit in reversed(jamcoin) :
        if bit == 1 :
            convert += current
        current*=base

    return convert

def inc_jamcoin(jamcoin) :
    carry=1
    for i,bit in reversed(list(enumerate(jamcoin[:-1]))) :
        if bit == 1 and carry == 1 :
            jamcoin[i] = 0
            continue

        if bit == 0 :
            jamcoin[i] = 1
            return

def is_good_jamcoin(jamcoin) :
    for base in range(2, 11) :
        base_jamcoin=jamcoin_to_int(jamcoin, base)
        if is_prime(base_jamcoin) :
            return False
    return True

def jamcoin_display(jamcoin) :
    to_display = "".join(map(str, jamcoin))

    for base in range(2, 11) :
        base_jamcoin=jamcoin_to_int(jamcoin, base)
        div=found_divide(base_jamcoin)
        if div == None :
            return False
        to_display += " " + str(div)
    print(to_display)
    return True

for caseno, line in enumerate(open("test.in", "r").readlines()[1:]) :
    problem=line.split()
    N=int(problem[0])
    J=int(problem[1])

    print("Case #%s:" % str(caseno+1))

    jamcoin = [0] * N
    jamcoin[0] = 1
    jamcoin[N-1] = 1
    for i in range(J) :
        while True :
            if is_good_jamcoin(jamcoin) :
                if jamcoin_display(jamcoin) :
                    break
            inc_jamcoin(jamcoin)
        inc_jamcoin(jamcoin)
