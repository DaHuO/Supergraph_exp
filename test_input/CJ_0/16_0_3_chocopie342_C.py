#!/usr/local/bin/python3
import sys
import math


def divisor(x):
    for i in range(2, int(math.sqrt(x))+1):
        if (x % i == 0):
            return i
    return 0


def base_b_number(x, b):
    res = 0
    mul = 1
    while (x != 0):
        if(x & 1):
            res += mul
        x >>= 1
        mul *= b
    return res


def jamcoin(i):
    d = [0 for x in range(11)]
    for b in range(2, 11):
        d[b] = divisor(base_b_number(i, b))
        if (d[b] == 0):
            break
#        print(base_b_number(i, b), file = sys.stderr)
        if (b == 10):
            print("{0:b}".format(i), end="")
            for bb in range(2, 11):
                print(" {0}".format(d[bb]), end="")
            print("")
            return True
    return False


def solve():
    tmp = input()
    tmp = tmp.split(" ")
    N = int(tmp[0])
    J = int(tmp[1])
    count = 0
    i = (1 << (N - 1)) + 1
    while (count < J):
        if (jamcoin(i)):
            count += 1
        i += 2

T = input()
for i in range(int(T)):
    print("Case #{0}:".format(i + 1))
    solve()
