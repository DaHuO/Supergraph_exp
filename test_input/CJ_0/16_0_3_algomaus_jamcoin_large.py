#! /usr/bin/env python

#no need to parse input, since input is always N=32, J=500

from math import sqrt
  
def nontrivial_divisor(x):
  if x < 2:
    return -1
  i = 2
  while i < min(int(sqrt(x)+1), 200):
    if x % i == 0:
      return i
    i = i + 1
  return -1

N = 32
J = 500
found = 0

print "Case #1:"

i = 2 ** (N-1) + 1

while i < 2 ** N:
  binaryString = format(i,'b')
  
  divisors = []
  for base in range(2, 11):
    num = int(binaryString, base)
    divi = nontrivial_divisor(num)
    if divi == -1:
      break
    else:
      divisors.append(divi)
  if len(divisors) == 9:
    found = found + 1
    print binaryString + " " + str(divisors[0]) + " " + str(divisors[1]) + " " + str(divisors[2]) + " " + str(divisors[3]) + " " + str(divisors[4]) + " " + str(divisors[5]) + " " + str(divisors[6]) + " " + str(divisors[7]) + " " + str(divisors[8])
  
  if found == J:
    break
  i = i + 2
