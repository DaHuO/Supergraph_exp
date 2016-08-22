#!/usr/bin/python

import re


def solve(line):
    different_signs = re.sub('\++', '+', line)
    different_signs = re.sub('-+', '-', different_signs)
    print(different_signs)
    times = len(different_signs) - 1
    if different_signs[-1] == '-':
        times += 1
    return times


def flip(fragment):
    new_fragment = ""
    for sign in fragment[::-1]:
        new_fragment += '+' if sign == '-' else '-'
    return new_fragment


def all_side_are_up(pile):
    return '-' in pile


with open('input.txt', 'r') as input:
    lines = input.read().splitlines()[1:]

    with open('output.txt', 'w') as output:
        for counter, line in enumerate(lines):
            solution = solve(line)
            output.write('Case #%s: %s \n' % (counter + 1, solution))
