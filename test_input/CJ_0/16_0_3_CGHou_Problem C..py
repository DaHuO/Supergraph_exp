# -*- coding: utf-8 -*-  
'''
Created on 9 Apr, 2016
https://code.google.com/codejam/contest/2270488/dashboard#s=a&a=0
@author: a0086303
'''

DATA_FILE_NAME = 'D-small-practice.in'
DATA_FILE_NAME = 'D-large-practice.in'
# DATA_FILE_NAME = 'B-large-practice.in'
# DATA_FILE_NAME = 'test_data_b.dat'
DATA_FILE_NAME = 'C_test.in'
SHELL_PIPE_FLAG = False

#==============================
import random
import math
from random import randint
from fractions import gcd
from Queue import Queue

# http://code.activestate.com/recipes/577037-pollard-rho-prime-factorization/

#from fractions import gcd
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def rabin_miller_1(p,k=20):
    if (p < 2):
        return False
    if (p != 2 and p % 2 == 0):
        return False
    s = p - 1
    while (s % 2 == 0):
        s >>= 1
    for i in xrange(k):
        a = random.randrange(p - 1) + 1
        temp = s
        mod = pow(a, temp, p)
        while (temp != p - 1 and mod != 1 and mod != p - 1):
            mod = (mod * mod) % p
            temp = temp * 2
        if (mod != p - 1 and temp % 2 == 0):
            return False
    return True

rabin_miller = rabin_miller_1

def pollard(n):
    if (n % 2 == 0):
        return 2;
    x = random.randrange(2, n) #x = random.randrange(2, 1000000)
    c = random.randrange(2, n) #c = random.randrange(2, 1000000)
    y = x
    d = 1
    while (d == 1):
        x = (x * x + c) % n
        y = (y * y + c) % n
        y = (y * y + c) % n
        d = gcd(x - y, n)
        if (d == n):
            break
    return d
def Pollard_Rho_Prime_Factorization_only_one(n):

    if (rabin_miller(n)):
       return n
    rst = n
    while rst == n:
        rst = pollard(n)
    return rst
# =================================================================


def data_iterator(lines_to_read=None):
    if not SHELL_PIPE_FLAG:
        with open(DATA_FILE_NAME, 'r') as f_handle:
            line_iter = f_handle.xreadlines()
            case_no = int(line_iter.next())
            for idx in range(case_no):
                if not lines_to_read:
                    line_no = int(line_iter.next())
                    # line_no = int(line_iter.next().split()[1])
                    yield idx + 1, [line_iter.next().strip() for _ in range(line_no + 1)]
                else:
                    yield idx + 1, [line_iter.next().strip() for _ in range(lines_to_read)]
    else:
        import sys  # raw_input() sys.stdin.readline()
        case_no = int(sys.stdin.readline())
        for idx in range(case_no):
            if not lines_to_read:
                line_no = int(sys.stdin.readline())
                yield idx + 1, [sys.stdin.readline().strip() for _ in range(line_no)]
            else:
                yield idx + 1, [sys.stdin.readline().strip() for _ in range(lines_to_read)]


result_out = ''


def solve(case_data):
    # from sympy.functions.combinatorial.numbers import nC, nP, nT
    # import bisect
    # from collections import Counter

    # N,X,K,A,B,C = map(int,case_data[0].split())
    N, dst_count = map(int,case_data[0].split())
    case_count = 0
    #dst_count = 3
    rst_list = []
    cal_set = set()
    a =  1 + 2 ** (N - 1)
    while case_count < dst_count:
        # print case_count,len(cal_set)
        # a = (random.randint(0, 2 ** (N - 2) - 1) << 1) + 1 + 2 ** (N - 1)
        # if a in cal_set:
        #     continue
        # else:
        #     cal_set.add(a)
        print case_count
        b = bin(a)[2:]
        br = b[::-1]
        #print a, b, br
        case_rst_list = [b]
        BREAK_FLAG = False
        for base in xrange(2, 11):
            n_base = 0
            for idx, c in enumerate(br):
                if c == '1':
                    n_base += base ** idx
            # print n_base,' '

            if (rabin_miller(n_base)):
                BREAK_FLAG = True
                break
            case_rst_list.append(str(Pollard_Rho_Prime_Factorization_only_one(n_base)))
        if not BREAK_FLAG:
            rst_list.append(' '.join(case_rst_list))
            case_count += 1
        a = a+2
    rst = '\n'.join(rst_list)
    return rst


for idx, case_data in data_iterator(lines_to_read=1):
    case_out = solve(case_data)
    # print case_data
    # print '========================'
    #result_tmp = 'Case #%d: %s\n' % (idx, case_out)
    # print case_out
    result_out = 'Case #1:\n'+ case_out
# print result_out

if not SHELL_PIPE_FLAG:
    import os

    if not os.path.exists('Out'):
        os.makedirs('Out')

    with open('./Out/' + DATA_FILE_NAME + '.out', 'wb') as f:
        f.write(result_out)

# with open(DATA_FILE_NAME+'.out','wb') as f:
#    f.write(result_out)
