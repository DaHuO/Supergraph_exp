#!/usr/bin/python27

import sys

def calc_base(num, base):
    div = int(base)
    tot = int(num[-1])
    if len(num) < 2:
        return tot
    for n in [ int(x) for x in num[-2::-1] ]:
        tot += n * div
        div *= int(base)
    return tot

def is_prime(num):
    i = 2
    while i < int(num):
        if (float(num) / float(i)).is_integer():
            return i
        i += i -1
    return -1

def one_prime(coin):
    divs = []
    for i in range(2,11):
        div = is_prime(calc_base(coin, i))
        if div == -1:
            return -1 
        divs.append(div)
    return divs

def increment_bin(num):
    bnum = calc_base(num, 2)
    bnum += 2
    newnum =  str(bin(bnum))[2:]
    if newnum.startswith('0'):
        raise Exception("Overflow bin!")
    return newnum

def get_next_coin(last):
    if not '1' in last:
        coin = '1'
        for x in range(len(last) -2):
            coin += '0'
        coin += '1'
    else:
        coin = last
    nextone = one_prime(coin)
    while nextone == -1:
        # increment coin
        coin = increment_bin(coin)
        nextone = one_prime(coin)
    return [coin] + nextone

c = sys.stdin.readline()

for cn in range(int(c)):
    [nlen, cnt] = sys.stdin.readline().strip().split(" ")
    last = ''.zfill(int(nlen))
    results = []
    for i in range(int(cnt)):
        coininfo = get_next_coin(last)
        results.append(coininfo)
        last = increment_bin(coininfo[0])

    print "Case #%d:" % (int(cn) + 1,)
    for j in range(len(results)):
        print "%s %d %d %d %d %d %d %d %d %d" % tuple(results[j])
