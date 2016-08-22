__author__ = 'pcjjman'
test_input = \
"""5
-
-+
+-
+++
--+-"""
test_output = \
"""Case #1: 1
Case #2: 1
Case #3: 2
Case #4: 0
Case #5: 3"""

import itertools
import math
import sys
test = False
line_number = 0


def get_input():
    global line_number
    if not test:
        return raw_input("")
    else:
        output = test_input.split("\n")[line_number]
        line_number += 1
        return output


def flip_pancakes(input_str, flip_point=0):
    input_str = list(input_str)
    for i in range(flip_point, len(input_str)):
        input_str[i] = '+' if input_str[i] == '-' else '-'
    return "".join(input_str)


if __name__ == "__main__":
    cases = int(get_input())
    for case in range(cases):
        pancakes = get_input()[::-1]
        #print pancakes, flip_pancakes(pancakes)
        flips = 0
        for i in range(len(pancakes)):
            if pancakes[i] == '-':
                pancakes = flip_pancakes(pancakes, i)
                flips += 1
        #print pancakes, flips
        # number of flips required:
        # number of 'bunches' of different colors
        # to simplify it we will simply iterate across the pancakes
        # and anytime we see one that is a -
        # flip the stack from that point
        print "Case #{}: {}".format(case + 1, flips)


