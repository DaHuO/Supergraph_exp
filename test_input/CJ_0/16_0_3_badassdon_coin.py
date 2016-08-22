import sys 
import math
import array
from itertools import *

T = 1

N = 32 - 1 # length
J = 500 # required # of jamcoins

# compute a sieve
compute_to = 100000
primes = []
sieve = array.array('i', (-1 for i in range(0, compute_to)))
for i in range(2, compute_to//2+1):
  if sieve[i] == -1:
    # this is prime, so add to rest of sieve
    primes.append(i)
    for j in range(2*i, compute_to, i):
      sieve[j] = i

def get_divisor_ish(n):
  # find some divisors
  for i in primes:
    if i == n:
      return -1

    if (n % i) == 0:
      return i

  # lets go ahead and assume it's prime-ish. we don't have to be entirely accurate,
  # since we're only looking for a certain number of jamcoins instead of all of them
  return -1 # prime

# generate all possible combinations of 0s and 1s to test for jamcoin
print "Case #1:"
found = 0

for i in islice(count(2**N), (2**(N+1))):
  if i % 2 == 0:
    continue

  jamcoin = ('{0:0' + str(N) + 'b}').format(i)
  divisors = [ ]
  for base in range(2, 11):
    interpretation = int(jamcoin, base)
    divisor = get_divisor_ish(interpretation)
    if divisor == -1:
      break
    divisors.append(divisor)

  if len(divisors) == 9:
    print "%s %s" % (jamcoin, " ".join(map(str,divisors)))
    found = found + 1
    #print

    #for base in range(2, 11):
    #  interpretation = int(jamcoin, base)
    #  divisor = get_divisor_ish(interpretation)
    #  print "%i: %i" % (interpretation, divisor)
    #print
    #print

  if found == J:
    break

