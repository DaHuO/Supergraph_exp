#!/usr/bin/python
# coding: utf-8
from __future__ import print_function
from __future__ import division
from math import sqrt
from itertools import count, islice
import random
import math
import sys

#nr_of_tasks = int(raw_input())

bins = []
bins2 = []

range_small = (16384,32767)
range_large = (1073741824,2147483647)


b = "10000000000000000000000000000000"


def check_if_prime(val):
    if val == 2:
       return True
    if val % 2 == 0:
        return False
    i = 3
    sqrt_val = math.sqrt(val)
    while i <= sqrt_val:
        if val % i == 0:
            return False
        i = i+2
    return True

def p_test(val):
    if (val > 1):
        for time in range(3):
            randomNumber = random.randint(2, val)-1
            if (pow(randomNumber, val-1, val) != 1):
                return False
        return True
    else:
        return False



def check_value(val):
    for i in range(2, 10 + 1):
        if p_test(int(val, i)):
            return False
    return True


jam_coins = []

def get_divisior_list(val):
    output = []
    for base in range(2, 10 + 1):
        value = int(val, base)
        count = 2
        for i in range(2, 500000):
            if value % i == 0:
                output.append(i)
                break

    if len(output) == 9:
        return output
    else:
        return False


counter = 0
for i in xrange(range_large[0],range_large[1]):
    bin_val = "".join([bin(i)[2:], "1"])
    if check_value(bin_val):
        counter = counter + 1
        jam_coins.append(bin_val)
        if len(jam_coins) == 5000:
            break


print("Case #{task}:".format(task=1))
lc = 0
for cj in jam_coins:
    list = get_divisior_list(cj)
    if not list == False:
        lc = lc + 1
        print("{} {}".format(cj, " ".join([str(item) for item in list])))
        if lc == 500:
            break
