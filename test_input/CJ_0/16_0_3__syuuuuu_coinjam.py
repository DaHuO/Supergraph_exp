import os
import itertools
from sys import argv
import math
from math import sqrt;
from itertools import count, islice

def main():
    outputLine = 'Case #1:'
    print outputLine

    N = 16
    J = 50
    coins = []

    low = int("1" * (N-1), 2) + 2
    high = int("1"+("0" * N), 2) - 1
    current = low

    while current <= high:
        currentStr = str_base(current, 2)
        divisors = []

        for base in range(2, 11):
            num = int(currentStr, base)
            if isPrime(num):
                break
            divisors.append(str(list(divisorGenerator(num))[1]))

        if len(divisors) == 9:
            divisors = [currentStr] + divisors
        if len(divisors) == 10:
            print ' '.join(divisors)
            coins = [divisors] + coins
        if len(coins) == J:
            break
        current = current + 2

def digit_to_char(digit):
    if digit < 10:
        return str(digit)
    return chr(ord('a') + digit - 10)

def str_base(number,base):
    (d, m) = divmod(number, base)
    if d > 0:
        return str_base(d, base) + digit_to_char(m)
    return digit_to_char(m)

def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

def divisorGenerator(n):
    large_divisors = []
    for i in xrange(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor

main()
