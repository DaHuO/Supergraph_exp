#!/usr/bin/python
# -*- coding: utf-8 -*-

import math
from itertools import product


def is_prime_or_give_me_a_non_trivial_divisor(n):
    result = 1  # to be returned if it's prime
    for divisor in range(2, int(math.sqrt(n)) + 1):
        if n % divisor == 0:
            result = divisor
            break
    return result


def is_jamcoin(str_n):
    is_jamcoin = True
    n_in_base_list = {}  # only useful if it's jaimcoin

    int_n_list = [int(str_digit) for str_digit in str_n]
    len_n = len(str_n)

    all_non_0_1 = [x for x in int_n_list if x not in [0, 1]]
    if len_n < 2 or int_n_list[0] != 1 or int_n_list[-1] != 1 or all_non_0_1:
        is_jamcoin = False
    else:
        for base in range(2, 11):
            if is_jamcoin:
                n_in_base = 0
                for j in range(0, len_n):
                    n_in_base += int_n_list[j] * int(
                        math.pow(base, len_n - 1 - j))
                divisor = is_prime_or_give_me_a_non_trivial_divisor(n_in_base)
                if divisor == 1:
                    is_jamcoin = False
                else:
                    n_in_base_list[n_in_base] = divisor
            else:
                break

    return (is_jamcoin,
            sorted(n_in_base_list.items(), key=lambda x: x[0]))


def generator(n):
    for c in product(['0', '1'], repeat=n):
        yield "".join(c)


def generate_jamcoins(n, j):
    # {jamcoin: list of 9 non-trivial divisors
    result = {}

    len_middle_part = n - 2
    g = generator(len_middle_part)
    maximum_generable = math.pow(2, len_middle_part)
    generated = 0
    while (generated < min(j, maximum_generable)):
        middle = ""
        for i in range(0, n - 1):  # ie range(0, n-2+1)
            pass  # middle +=
        s = "1" + g.next() + "1"
        is_jamcoin_tuple = is_jamcoin(s)
        if is_jamcoin_tuple[0]:
            result[s] = [divisor for (_, divisor) in is_jamcoin_tuple[1]]
            generated += 1
    return result


t = int(raw_input())
for i in xrange(1, t + 1):
    n, j = [int(s) for s in raw_input().split(" ")]
    print("Case #{}:".format(i))
    for jamcoin, divisors in generate_jamcoins(n, j).items():
        print("{} {}".format(jamcoin,
                       "".join([str(e) + " " for e in divisors]).rstrip()))
