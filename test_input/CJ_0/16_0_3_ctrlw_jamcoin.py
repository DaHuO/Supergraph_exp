#!/usr/bin/python3
import sys, math, re, bisect
from operator import add

cache = {}

# just use the first primes
primes = [ 2,   3,   5,   7,  11,  13,  17,  19,  23,  29,  31,  37,  41,
  43,  47,  53,  59,  61,  67,  71,  73,  79,  83,  89,  97, 101,
 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167,
 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239,
 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313,
 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397,
 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467,
 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569,
 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643,
 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733,
 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823,
 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911,
 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

'''return non-trivial divisor or 0'''
def get_divisor(x):
  if x in cache:
    return cache[x]
  
  result = 0
  #iterate over primes and see which one is a divisor
  for prime in primes:
    #print(x, prime)
    sq = prime * prime
    if sq == x:
      result = prime
      break
    elif sq > x:
      break
    elif x % prime == 0:
      result = prime
      break
      
  cache[x] = result
  return result

def generate_values(s):
  result = [0] * 9
  for i in range(9):
    result[i] = int(s, i+2)
  return result

def get_values(x):
  s = "{0:b}".format(x)
  values = generate_values(s)
  #print(s, values)
  divisors = []
  for v in values:
    d = get_divisor(v)
    if not d:
      return s, []
    divisors.append(d)
  return s, divisors

def generate_bounds(n, max_count):
  lower = int("1" + ("0" * (n-2)) + "1", 2)
  upper = int("1" + ("1" * (n-2)) + "1", 2)
  
  count = 0
  for i in range(lower, upper + 1, 2):
    s, divisors = get_values(i)
    if divisors:
      print(s, " ".join(map(str, divisors)))
      count += 1
      if count >= max_count:
        break
      

#generate_bounds(6)
#generate_bounds(32)
#sys.exit()
    
T = int(sys.stdin.readline())
for t in range(T):
  print( "Case #%d:" % (t + 1))
  (N, J) = map(int, sys.stdin.readline().strip().split())
  generate_bounds(N, J)


