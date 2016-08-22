import string
from math import sqrt

_result = open("./result.txt", "w")
_result.write("Case #1:\n")

digits = 32
amount = 500

def toStr(n,base):
  convertString = "0123456789ABCDEF"
  if n < base:
    return convertString[n]
  else:
    return toStr(n//base,base) + convertString[n%base]

def isPrime2(number):
    if(number <= 1):
        return False
    if(number > 2) and (number%2 == 0):
        return False

    j = sqrt(number)
    i = 3
    while(i < j+2 and i < 10000):
        if(number % i == 0):
            return False
        i += 1
    return True

def getADivisor(number):
  if number == 1 or number == 2:
    return number

  j = sqrt(number)
  i = 2
  while(i < j+1):
    if(number % i == 0):
      return i
    i += 1
  return number

def primes_bools(limit):
  a = [True] * limit                          # Initialize the primality list
  a[0] = a[1] = False

  for (i, isprime) in enumerate(a):
    if isprime:
      for n in xrange(i*i, limit, i):     # Mark factors non-prime
        a[n] = False

  return a

# primes = []
# for key in primes_sieve(10000000):
#   primes.append(key)
# print len(primes)
#
primes = primes_bools(1000000)
print len(primes)

def isPrime(number):
  global primes

  if number < 1000000:
    return primes[number]
  else:
    return True
    # return isPrime2(number)

print isPrime(7)
print isPrime(17)
print isPrime(27)

lowest_number = 2 ** (digits - 1) + 1
highest_number = 2 ** digits - 1

# print lowest_number
# print toStr(lowest_number, 2)
# print highest_number
# print toStr(highest_number, 2)

found = 0
while found < amount and lowest_number <= highest_number:
  prime = False
  bool_number = toStr(lowest_number, 2)
  # print "\n\n"
  # print bool_number

  for i in range(2, 11):
    number = int(bool_number, i)

    # print i, number

    if isPrime2(number):
      prime = True
      break

  if not prime:
    results = [bool_number]
    for i in range(2, 11):
      results.append(getADivisor(int(bool_number, i)))

    result = " ".join(map(str,results))
    print result
    _result.write(result + "\n")
    found += 1

  lowest_number += 2

_result.close()
