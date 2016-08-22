#!/usr/bin/env python2.7

import math
import sys

max_to_gen = int(math.sqrt(int("1" * 16))) + 1  # small case
sieve = [True] * max_to_gen
sieve[0] = 2
sieve[1] = 3
sieve_ptr = 2

def maybe_primes():
  num = 5
  while True:
    yield num
    yield num + 2
    num += 6

for num in maybe_primes():
  if num >= max_to_gen:
    break
  if sieve[num]:
    sieve[sieve_ptr] = num
    sieve_ptr += 1
    for num2 in range(num + num, max_to_gen, num):
      sieve[num2] = False

del sieve[sieve_ptr:]

def find_divisor(num):
  for divisor in sieve:
    if num % divisor == 0:
      return divisor
    if divisor * divisor >= num:
      return None

T = int(raw_input())
for iT in range(1, T + 1):
  N, J = map(int, raw_input().split())
  print "Case #%s:" % iT
  Nm2 = N - 2
  curval = [0] * Nm2
  ws = [[which_base ** which_pos for which_pos in range(1, N - 1)] for which_base in range(2, 11)]
  cursums = [which_base ** (N - 1) + 1 for which_base in range(2, 11)]
  # try everything
  divisors = [0] * len(cursums)
  found = 0
  while found < J:
    print >> sys.stderr, found, cursums
    for i in range(len(cursums)):
      divisor = find_divisor(cursums[i])
      if divisor is None:
        divisors[0] = None
        break
      divisors[i] = divisor
    if divisors[0] is not None:
      print cursums[-1], " ".join(map(str, divisors))
      sys.stdout.flush()
      found += 1
    # +1
    incp = 0
    while incp < Nm2:
      if curval[incp] == 0:
        curval[incp] = 1
        cursums = [cursum + w[incp] for cursum, w in zip(cursums, ws)]
        break
      else:
        curval[incp] = 0
        cursums = [cursum - w[incp] for cursum, w in zip(cursums, ws)]
        incp += 1
    if incp >= Nm2: break
