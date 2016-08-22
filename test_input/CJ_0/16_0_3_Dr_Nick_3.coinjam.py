#!/usr/bin/env python

import sys

def num2vector(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n /= b
    return digits[::-1]

def vec2num(v, b):
  res = 0
  mult = 1
  for i in v[::-1]:
    res += i*mult
    mult *= b
  return res

cases = int(sys.stdin.readline().strip())

for c in range(1,cases+1):
  
  N, J = map(int, sys.stdin.readline().split())
  found = 0

  print "Case #%d:" %c
  for n in xrange(2**N/2+1, 2**N, 2):
    binary_n = num2vector(n, 2)

    mults = []
    for b in range(2, 11):
      n = vec2num(binary_n, b)

      #we have plenty of jamcoins to check so abort difficult ones
      for i in range(2, min(n/2+1, 10000)): 
        if(n % i  == 0):
          mults.append(i)
          break

    if len(mults) == 9:
      print n, " ".join(map(str,mults))
      found+=1
      if found == J:
        sys.exit(0)
     
