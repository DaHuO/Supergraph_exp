#!/usr/bin/env python

__author__ = 'Bill'

from misc import input_, output_

num_cases, cases = input_('A-large.in')


Results = []

for case in cases:
    answ = case[0]
    case = case.rstrip('\n')
    for letter in case[1:]:
        if (letter < answ[0]):
            answ += letter
        else:
            answ = letter + answ
    Results.append(answ)





output_(Results, 'A-large.out')