import sys
import math
import random

def read_one_line():
  return sys.stdin.readline().rstrip()


def is_prime(num):
  if num == 2:
    return True, None
  elif num <= 1:
    return False, None
  elif num % 2 == 0:
    return False, num//2

  sqr = int(math.sqrt(num)) + 1

  #for i in range(2, num):
  #  print num, i
  #  if num % i == 0 and i != 1 and i != num:
  #    return False, i

  for divisor in range(3, sqr, 2):
    if num % divisor == 0 and divisor != 1 and divisor != num:
      return False, divisor

  return True, None


def gen_jamcoin(length):
  if length == 2: return '11'

  content_length = length - 2

  while True:
    coin_content = ''.join([str(random.randint(0, 1)) for i in xrange(content_length)])
    coin = '1%s1' % coin_content

    reprs = [int(coin, base) for base in xrange(2, 11)]
    divisors = []

    for num in reprs:
      prime, divisor = is_prime(num)

      if not prime:
        divisors.append(divisor)
      else:
        break

    if len(divisors) == len(reprs):
      break

  return coin, divisors

if __name__ == '__main__':
  num_cases = int(read_one_line())

  for case in xrange(num_cases):
    N, J = [int(c) for c in read_one_line().split(' ')]
    coins = []
    divisors = []

    while len(coins) != J:
      coin, divisor = gen_jamcoin(N)

      if coin in coins:
        continue

      coins.append(coin)
      divisors.append(divisor)

    print 'Case #%d:' % (case + 1)

    for i in xrange(len(coins)):
      print '%s %s' % (coins[i], ' '.join([str(d) for d in divisors[i]]))

