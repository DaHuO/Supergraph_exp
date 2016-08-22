"""Usage:
    pypy -u X.py < X-test.in > X-test.out
or sometimes:
    python -u X.py < X-test.in > X-test.out
may be python 2 or 3.
"""
from __future__ import print_function

import sys


def common_setup():
    pass


def case_reader(tc, infile):
    T = next(infile).strip()
    del infile
    return locals()


def case_solver(tc, N=None, P=None, I=None, T=None, S=None, **kwargs):
    end = len(T)
    res = ['', '']
    while end > 0:
        fl = sorted(T[:end])[-1]
        i = T[:end].rindex(fl)
        res[0] += fl
        res[1] = T[i + 1:end] + res[1]
        end = i
    return 'Case #{:d}: {}'.format(tc, res[0] + res[1])


if __name__ == '__main__':
    common_setup()
    cases = [case_reader(tc, sys.stdin) for tc in range(1, int(next(sys.stdin)) + 1)]
    for case in cases:
        print(case_solver(**case))
