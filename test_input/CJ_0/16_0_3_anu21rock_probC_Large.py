#!/usr/bin/env python
#-*- coding:utf-8 -*-

import itertools

XNUMBER = 32


def check(S):
    aall = []
    for i in range(2,11):
        num = int(S, base=i)
        de = [i for i in allSievePrimes if i < num **0.5]
        calc = sum([num%i==0 for i in de])
        if calc == 0: return False
        aall.append([ix for ix in de if num%ix==0 ][0])
    return aall


def SievePrimes(n):
    sieve = [True] * (n/2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]



a = itertools.product("01",repeat = XNUMBER - 2)
allSievePrimes = SievePrimes(10**6)

na = 0
with open("Coins_Large.txt","wb") as fe:
    fe.write("Case #1:\n")
    for i in range(1500):
        s = "1"+"".join(a.next()) + "1"
        #print int(s, 2)
        xa = check(s)
        if xa:
            print s, " ".join(map(str,xa))
            fe.write(s+" "+" ".join(map(str,xa))+"\n")
            na += 1
        if na == 500 : break

