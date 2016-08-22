#!/usr/bin/env python

BASES = range(2, 11)
CACHE = {}
PRIMES = {}

def isprime(n):
  n = abs(int(n))
  if n < 2:
    return False
  if n == 2:
    return True
  if not n & 1:
    return False
  for x in range(3, int(n**0.5) + 1, 2):
    if n % x == 0:
      return False
  return True


def prime_test(n):
  if n not in PRIMES:
    PRIMES[n] = isprime(n)
  return PRIMES[n]


def canidate_range(lenght):
  n = int('1' * (lenght - 2), 2)
  return xrange(n+1)


def nontrivial_divisor(n):
  if n not in CACHE:
    for i in xrange(2, n//2 + 1):
      if n % i == 0:
        CACHE[n] = i
        break
  return CACHE[n]


def valid_coin(coin):
  nontrivial_divisors = []
  for base in BASES:
    n = int(coin, base)
    if prime_test(n):
      return False
    divisor = nontrivial_divisor(n)
    if divisor:
      nontrivial_divisors.append(divisor)
    else:
      return False
  return ' '.join([ str(i) for i in nontrivial_divisors])


def foo(lenght):
  lenght = int(lenght)
  template = "1{{0:0{0}b}}1".format(lenght-2)
  for coin in (template.format(i) for i in canidate_range(lenght)):
    validate_coin = valid_coin(coin)
    if validate_coin:
      yield '{0} {1}'.format(coin, validate_coin)


t = int(raw_input())  # read a line with a single integer


for case in xrange(1, t + 1):
  count = 0
  l, n = str(raw_input()).split()
  n = int(n)

  print "Case #{}:".format(case)

  for coin in foo(l):
    print coin
    count += 1
    if count == n: break
