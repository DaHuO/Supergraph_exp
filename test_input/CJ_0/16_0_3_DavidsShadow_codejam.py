#!/usr/bin/python2.7
# codejam.py
import math

N = 16
J = 50
RADIX = list(range(2,11))

print "Case #1:"

def find_divisor(n):
  """
  Find the smallest nontrival divisor of n, return 0 if none are found.
  """
  if n > 3:
    for i in xrange(2, int(math.sqrt(n))+1):
      q, r = divmod(n, i)
      if r == 0:
        return q

  return 0

# Given that, the first digit is 1 and the last digit is 1
# determine the base 10 bounds. Because the last digit is 1 
# we do not need to consider even numbers.

start = 2**(N-1) + 1
end = sum(2**n for n in xrange(N))

ujc = 0 # unique jamcoins
for v in xrange(start, end+1, 2):
    if ujc >= J: # exit if already found J jamcoins
      break
    
    pjc = bin(v)[2:]
    output = [pjc]
    for r in RADIX:
      d = find_divisor(int(pjc, base=r))
      if d:
        output.append(str(d))
      else:
        break
 
    if len(output) == 10: # divisors at each base  
      print  " ".join(output)
      ujc += 1
