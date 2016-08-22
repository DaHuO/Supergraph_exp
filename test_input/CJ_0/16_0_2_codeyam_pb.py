#!/usr/bin/env python
# Python 3

import itertools

# Answer is just the number of groups of either character (- or +),
# after you drop the final group of '+'s, if there is one


def pb(s):
    keys = []
    for k, g in itertools.groupby(s):
        keys.append(k)

    if keys[-1] == "+":
        keys = keys[:-1]

    return len(keys)

# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    s = str(input())
    print("Case #{}: {}".format(i, pb(s)))
    # check out .format's specification for more formatting options
