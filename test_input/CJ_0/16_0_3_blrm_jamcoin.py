#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

def _is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in xrange(3, int(math.sqrt(n)) + 1, 2))

def _nontrivial_divisor(num):
  for i in xrange(3,num):
    if (num % i) == 0:
        return i

def _is_valid_jamcoin(num):
  for i in _coin_bases(num):
    if _is_prime(i):
      return False
  else:
    return True

def _coin_bases(coin):
  """ Return a list of the jamcoin interpreted in bases 2 - 10"""
  return [int(coin,base=i) for i in range(2,11)]

def generate_jamcoins(N, J):
  """ Returns J valid jamcoins of length N,
      and a list of nontrivial divisors for
      the jamcoins representation in bases
      2 - 10 inclusive.
  """
  total_coins = 0
  candidate = '1' + ('0'*(int(N)-2)) + '1'
  while total_coins < int(J):
    if _is_valid_jamcoin(candidate):
      output = ' '.join([str(_nontrivial_divisor(i)) for i in _coin_bases(candidate)])
      print "{} {}".format(candidate, output)
      total_coins += 1
    # increment the candidate by + 2, so that it still ends with 1
    candidate = bin(int(candidate,base=2)+2).lstrip('0b')

if __name__ == "__main__":
  testcases = input()
  for caseNr in xrange(1, testcases+1):
    test_args = raw_input().split()
    print("Case #%i:" % (caseNr))
    generate_jamcoins(*test_args)

