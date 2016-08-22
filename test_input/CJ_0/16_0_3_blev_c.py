
import math
from sys import stdin
def readline(): return stdin.readline().strip('\n')
def readint(): return int(readline())
def readlineints(): return [int(x) for x in readline().split(' ')]


def getinbase(c, base):
   y = c
   n = 0
   digit = 0
   while y > 0:
      if y & 1: n += base**digit
      digit += 1
      y >>= 1
   return n


def finddivisor(n):
   upper = min(int(math.sqrt(n)), 2000)
   for i in xrange(2, upper):
      if n % i == 0: return i
   return -1


def isjamcoin(c):
   divisors = []
   for base in range(2, 11):
      n = getinbase(c, base)
      d = finddivisor(n)
      if d == -1: return []
      divisors.append(d)
   return divisors

T = readint()

for t in range(1, T+1):
   N, J = readlineints()
   # find J jamcoins of length N
   jamcoins = {}
   c = (1 << (N-1)) + 1
   while len(jamcoins) < J:
      result = isjamcoin(c)
      if len(result) > 0:
         jamcoins[c] = result
      c += 2

   print 'Case #' + str(t) + ':'
   for jc, divs in jamcoins.iteritems():
      print bin(jc)[2:], ' '.join([str(d) for d in divs])
  

