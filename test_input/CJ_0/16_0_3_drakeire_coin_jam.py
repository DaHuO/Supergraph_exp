#!/usr/bin/env python3

import sys
from itertools import product
import math

def main():
  fi = sys.stdin
  fo = sys.stdout
  case_count = int(fi.readline().strip())
  for i in range(1, case_count+1):
    n, j = read_input(fi)
    solution = solve(n, j)
    display_and_clear(fo, i, solution)

def read_input(f):
  n, j = [int(token) for token in f.readline().split()]
  return n, j

def display_and_clear(f, i, jamcoins):
  f.write('Case #%d:\n' % i)
  for coin in jamcoins:
    f.write(coin[0])
    for divisor in coin[1]:
      f.write(' %d' % divisor)
    f.write('\n')
  f.flush()

def solve(n, j):
  jamcoins = []
  for mid in product(['0', '1'], repeat=n - 2):
    coin_candidate = ''.join(['1'] + list(mid) + ['1'])
    valid, divisors = test_jamcoin_candidate(coin_candidate)
    if valid:
      jamcoins.append((coin_candidate, tuple(divisors)))
      if len(jamcoins) == j:
        break
  
  return jamcoins

def test_jamcoin_candidate(candidate):
  divisors = []
  for i in range(2, 11):
    interpretation = int(candidate, base=i)
    prime, divisor = is_prime(interpretation)
    if prime:
      return False, []
    else:
      divisors.append(divisor)
  return True, divisors
    
def is_prime(n):
  if n < 2:
    return False, None

  if n == 2:
    return True, None

  if n % 2 == 0:
    return False, 2

  limit = int(math.ceil(math.sqrt(n))) 
  for i in range(3, limit, 2):
    if n % i == 0:
      return False, i

  return True, None

if __name__ == '__main__':
  main()

