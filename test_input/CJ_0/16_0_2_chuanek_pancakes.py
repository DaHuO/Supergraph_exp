#!/usr/bin/python3

import sys


def changes(pancakes, last_val):
    i = len(pancakes) - 1
    change = 0
    while i >= 0:
        if last_val != pancakes[i]:
            if last_val == "+":
                last_val = '-'
            else:
                last_val = '+'
            change += 1
        i -= 1
    return change


def get_output(input_val):
    num_flips = changes(input_val, '+')
    return num_flips


def flip(pancakes):
    return "".join(reversed(pancakes))


if __name__ == "__main__":
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        print("Case #{}: {}".format(i, get_output(input())))
