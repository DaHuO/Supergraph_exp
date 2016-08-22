import numpy, sys

def primesfrom3to(n):
    """ Returns a array of primes, 3 <= p < n """
    sieve = numpy.ones(n/2, dtype=numpy.bool)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = False
    return 2*numpy.nonzero(sieve)[0][1::]+1

N = 16
J = 50
BASES = [2,3,4,5,6,7,8,9,10]

from bisect import bisect_left
import math
N_PRECALC = int('1' * N, 10)
XX = int(math.sqrt(N_PRECALC))
__primes = primesfrom3to(XX)
def is_prime(n):
    # if prime is already in the list, just pick it
    if n <= XX:
        i = bisect_left(__primes, n)
        return i != len(__primes) and __primes[i] == n
    # Divide by each known prime
    limit = int(n ** .5)
    for p in __primes:
        if p > limit: return True
        if n % p == 0: return False
    raise 'fuck'

# naive implementation
def _find_factor(n):
  for i in range(2, 1+n//2):
    if n % i == 0: return i
  raise 'oops'

def find_factor(n):
    # if prime is already in the list, just pick it
    if n <= XX:
        i = bisect_left(__primes, n)
        prime = (i != len(__primes) and __primes[i] == n)
        if prime:
          return None
        else:
          return _find_factor(n)
    # Divide by each known prime
    limit = int(n ** .5)
    for p in __primes:
        if p > limit: return None
        if n % p == 0: return p
    raise 'oops'

def find_factors_in_bases(cjstr):
  factors = []
  for b in BASES:
    in_base = int(cjstr, b)
    factor = find_factor(in_base)
    if not factor:
      # print('%s base %d (%d decimal) is prime' % (cjstr, b, in_base))
      return None
    factors.append(factor)
  return factors

def is_prime_in_any_base(cjstr):
  for b in BASES:
    in_base = int(cjstr, b)
    prime = is_prime(in_base)
    if prime:
      # print('%s base %d (%d decimal) is prime' % (cjstr, b, in_base))
      return True
  return False

def coinjams():
  coins = []
  i = 1 + 2 ** (N - 1)
  while len(coins) < J:
    coin = format(i, 'b')
    i += 2
    factors = find_factors_in_bases(coin)
    if factors:
      coins.append(coin)
      print('%s %s' % (coin, ' '.join([str(x) for x in factors])))
  return coins

#jams = coinjams()
print('Case #1:')
coinjams()
#for cj in jams:
#  print(cj)
