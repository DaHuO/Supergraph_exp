import itertools
import math


def to_str(i, base=10):
    if i == 0:
        return '0'

    def rec(i):
        if i == 0:
            return ''
        return rec(i/base) + str(i % base)

    return rec(i)


def gen_jamcoin_candidates(length):
    for i in xrange(2**(length-2)):
        yield to_str((i << 1) + 2**(length-1) + 1, 2)
