#!/usr/bin/env python

from __future__ import division, print_function
import math

def lcd(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return i
    return False

def get_divisors(jamcoin_str):
    divisors = [ ]
    for i in range(2, 11):
        jamcoin_val = int(jamcoin_str, i)
        jamcoin_lcd = lcd(jamcoin_val)
        if jamcoin_lcd is not False:
            divisors.append(lcd(jamcoin_val))
        else:
            return False
    return divisors

def generate_possible_jamstrings(n):
    def generate_possible_strings(n):
        if n == 1:
            yield "0"
            yield "1"
        else:
            for i in generate_possible_strings(n-1):
                yield "0" + i
                yield "1" + i
    for i in generate_possible_strings(n-2):
        yield "1" + i + "1"

def generate_j_jamcoins_length_n(n, j):
    # n is length of jamstring,
    # j is number of jamstrings to output
    jamstrings = [ ]
    for i in generate_possible_jamstrings(n):
        divisors = get_divisors(i)
        if divisors is not False:
            jamstrings.append((i, divisors))
        if len(jamstrings) == j:
            return jamstrings

if __name__ == '__main__':
    T = int(raw_input())
    for i in range(T):
        print("CASE #{}:".format(i+1))
        jamstrings = generate_j_jamcoins_length_n(*map(int, raw_input().split()))
        for jam, divs in jamstrings:
            print(jam, end = ' ')
            print(" ".join(map(str, divs)))

