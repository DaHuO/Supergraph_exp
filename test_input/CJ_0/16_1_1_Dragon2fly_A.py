#!/usr/bin/env python 
# -*- coding: utf-8 -*-
__author__ = 'duc_tin'

"""
    The Last Word
"""


def get_lastword():
    my_word = S[0]
    for c in S[1:]:
        if c >= my_word[0]:
            my_word=c+my_word
        else:
            my_word+=c

    return my_word

T = int(raw_input())

for case in range(1, T + 1):
    S = raw_input()
    last_word = get_lastword()
    print 'Case #%d: %s' % (case, last_word)
