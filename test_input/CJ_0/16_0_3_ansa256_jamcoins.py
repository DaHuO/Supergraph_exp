#!/usr/bin/env python3

import sys
import re
import random
import functools
import array

def non_trivial_factor(n):
  for i in range(2, 10):
    if (n % i == 0 and n != i):
      return i

def to_binary_string(n):
  return "{0:b}".format(n)


file  = open(sys.argv[1])
total = int(file.readline())

for i in range(1, total + 1):
  n, j = map(int, file.readline().split())
  low = 2 ** (n - 3)
  high = 2 ** (n - 2) - 1

  print("Case #%d:" % i)

  jamcoins = []
  current = high

  while len(jamcoins) != j:
    coin  = "1" + to_binary_string(current) + "1"
    current -= 1

    bases = [int(coin, b) for b in range(2, 11)]
    non_trivials = [non_trivial_factor(b) for b in bases]

    if (any(nt is None for nt in non_trivials)):
      continue

    divisors = [str(nt) for nt in non_trivials]

    print("%s %s" % (coin, " ".join(divisors)))
    jamcoins.append(coin)
