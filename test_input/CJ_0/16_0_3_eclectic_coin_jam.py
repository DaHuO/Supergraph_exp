#!/usr/bin/python3
import sys
import random
import functools
import numpy as np

T = int(input())
if T != 1:
    raise Exception('T != 1', T)
N, J = tuple(map(int, input().split(" ")))


def is_probable_prime(n, k = 7):
   """use Rabin-Miller algorithm to return True (n is probably prime)
      or False (n is definitely composite)"""
   if n < 6:  # assuming n >= 0 in all cases... shortcut small cases here
      return [False, False, True, True, False, True][n]
   elif n & 1 == 0:  # should be faster than n % 2
      return False
   else:
      s, d = 0, n - 1
      while d & 1 == 0:
         s, d = s + 1, d >> 1
      # Use random.randint(2, n-2) for very large numbers
      for a in random.sample(range(2, min(n - 2, sys.maxsize)), min(n - 4, k)):
         x = pow(a, d, n)
         if x != 1 and x + 1 != n:
            for r in range(1, s):
               x = pow(x, 2, n)
               if x == 1:
                  return False  # composite for sure
               elif x == n - 1:
                  a = 0  # so we know loop didn't continue to end
                  break  # could be strong liar, try another a
            if a:
               return False  # composite if we reached end of this loop
      return True  # probably prime if reached end of outer loop

def GetDivisor(N, k = 30, i_max = None, i_parallel=0, n_parallel=1):
    prime = is_probable_prime(N, k = k)
    if prime:
        raise Exception('Prime!?')
    if i_max == None:
        i_max = int(N**0.5) + 2
    i_min = 2
    i_interval = (i_max-i_min)//n_parallel
    i_min_loc = i_min + i_interval*i_parallel 
    i_max_loc = i_min + i_interval*(i_parallel+1) +1
    # print(i_parallel, n_parallel, i_min_loc, i_max_loc, i_max)
    for i in range(i_min_loc, i_max_loc):
        # print(i,N,N % i)
        if N % i == 0:
            return i
    return None
    # raise Exception('No Divisor found', i_base, test_str, rep)
    # return set(functools.reduce(list.__add__, 
    #     ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n /= b
    return digits[::-1]

def FindJamCoin_BruteForce(N, k=7, J=1E5, n_start=None):
    ini_test_str = '1'+'0'*(N-2)+'1'
    end_test_str = '1'*N
    if n_start == None:
        n_start = int(ini_test_str,2)
    n_end   = int(end_test_str,2)
    # print('n_start, n_start, diff', n_start, n_end, n_end-n_start)

    for i_N in range(n_start, n_end+1, 2):
        test_str = "".join(map(str,numberToBase(i_N, 2)[-N:]))
        res = FastCheckIfJamCoin(test_str, k=k)
        if res: # found_jamcoin!
            return test_str, i_N
    #         # print('found_jamcoin!')
    #         found_jamcoin.append(test_str)
    #         if len(found_jamcoin) >= J:
    #             break
    # return found_jamcoin

def GetDivisors(test_str, n_parallel=1, i_max=10000):
    divisors = list()
    reps     = list()
    for i_base in range(2,11):
        div = None
        rep = int(test_str,i_base)
        try:
            for i_parallel in range(n_parallel):
                div = GetDivisor(rep, i_max = i_max, i_parallel=i_parallel, n_parallel=n_parallel)
                if div != None:
                    # print('Got it!', i_base, rep, i_parallel, n_parallel, div)
                    raise Exception('Got it!')
        except Exception as e:
            # print(e)
            # print('Got it!', i_base, rep, i_parallel, n_parallel, div)
            pass
        if div == None:
            # print(test_str, i_base, rep, div)
            raise Exception('real problem!')
        reps.append(rep)
        divisors.append(div)
        # print(rep, div, rep % div)
    return divisors, reps
        # print(test_str, i_base, rep, divs)

def FastCheckIfJamCoin(test_str, k=7):
    if test_str[0] != '1' and test_str[-1] != '1':
        return False
    for i_base in range(2,11):
        rep = int(test_str,i_base)
        # print(rep)
        if is_probable_prime(rep, k=k):
            return False # if prob prime we continue, it's not sure but this is enough ..
    return True

def DoubleCheckIfJamCoint(test_str, divisors):
    for i_base in range(2,11):
        rep = int(test_str,i_base)
        if rep % divisors[i_base-2] != 0:
            raise Exception('No jamcoin!', test_str, i_base, rep, divisors[i_base-2], rep % divisors[i_base-2])
    return True


# Testing
# test_strs = ['100011','111111','111001']
# divisors = np.array([[5,13,147,31,43,1121,73,77,629],
#                      [21,26,105,1302,217,1032,513,13286,10101],
#                      [3,88,5,1938,7,208,3,20,11]])
# for st, div in zip(test_strs,divisors):
#     print(st, div, DoubleCheckIfJamCoint(st, div))

n_start = None
found_jamcoins = list()
print("Case #{}:".format(1))
while len(found_jamcoins) < J:
# for i_J in range(J):
    jamcoin, n_end = FindJamCoin_BruteForce(N, k=7, J=5*J, n_start=n_start)
    n_start = n_end + 2
    try:
        divisors, reps = GetDivisors(jamcoin, n_parallel=1, i_max=int(1E4))
        if DoubleCheckIfJamCoint(jamcoin, divisors):
            print(jamcoin, " ".join(map(str,divisors)))
        found_jamcoins.append(jamcoin)
    except Exception as e:
        pass
        # print(e)
        # print('did not find a divisor')