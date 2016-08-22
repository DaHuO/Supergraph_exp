#!/usr/bin/env python

from math import sqrt

T = int(raw_input())

saved = {}

# primality
def findDivisor(n):
  if n == 1:
    return 1
  if n in saved:
    return saved[n]
  for i in range(2, int(sqrt(n))+1):
    if n % i == 0:
      saved[n] = i
      #print 'save', n, i
      return i
  #print 'save', n, None
  saved[n] = None
  return None

def coinToDec(coin, base):
  o = 0
  for d in coin:
    o *= base
    o += int(d)
  return o

def isJamcoin(coin):
  divisors = []
  for base in range(2, 11):
    v = coinToDec(coin, base)
    #print coin, base, v
    divisor = findDivisor(v)
    if not divisor:
      return None
    divisors.append(divisor)
  return divisors
    
def iterCoin(n, j):
  coins = []
  if n == 2:
    coin = '11'
    div = isJamcoin(coin)
    if div:
      coins.append((coin, div))
    return coins
  for i in range(0, 2**(n-2)):
    midBin = bin(i)[2:]
    coin = '1' + '0'*(n-2-len(midBin)) + midBin + '1'
    div = isJamcoin(coin)
    if div:
      #print 'jam', coin, div
      coins.append((coin, div))
    if len(coins) == j:
      return coins

def read_problem():
  n, j = [ int(e) for e in raw_input().split() ]
  return n, j

def solve(problem):
  n, j = problem
  coins = iterCoin(n, j)
  o = '\n'
  for coin in coins:
    o += '%s' % coin[0]
    for d in coin[1]:
      o += ' %d' % d
    o += '\n'
  return o[:-1]

for n in range(T):
  problem = read_problem()
  solution = solve(problem)
  print 'Case #%d:%s' %(n+1, solution)

