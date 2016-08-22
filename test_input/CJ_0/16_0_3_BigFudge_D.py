#!/usr/bin/env python
import random

def _try_composite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2**i * d, n) == n-1:
            return False
    return True # n  is definitely composite
 
def miller_rabin(n, _precision_for_huge_n=16):
    if n in _known_primes or n in (0, 1):
        return True
    if any((n % p) == 0 for p in _known_primes):
        return False
    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1
    # Returns exact according to http://primes.utm.edu/prove/prove2_3.html
    if n < 1373653: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3))
    if n < 25326001: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5))
    if n < 118670087467: 
        if n == 3215031751: 
            return False
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7))
    if n < 2152302898747: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11))
    if n < 3474749660383: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13))
    if n < 341550071728321: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17))
    # otherwise
    return not any(_try_composite(a, d, n, s) 
                   for a in _known_primes[:_precision_for_huge_n])
 
_known_primes = [2, 3]
_known_primes += [x for x in range(5, 1000, 2) if miller_rabin(x)]

def is_prime(n):
    if n < 2:
        return False
    else:
        return miller_rabin(n)

def prime_generator(n=2):
    if n <= 2:
        yield 2
    n += 1 if n % 2 == 0 else 0
    while True:
        while is_prime(n) == False:
            n += 2
        yield n
        n += 2

def read_stdin_lines():
    import fileinput
    return [line for line in fileinput.input()]

def parse_lines(lines):
    lines = lines[1:]
    return [map(int, l.split(' ')) for l in lines]

def to_jam_coin(x, N):
    fmt_str = '1{0}:0{N}b{1}1'.format('{', '}', N=N-2)
    return fmt_str.format(x)

def is_jam_coin(coin):
    for base in range(2,11):
        if is_prime(int(coin, base)):
            return False
    return True

def divisors(coin):
    ds = []
    for base in range(2, 11):
        n = int(coin, base)
        for p in prime_generator():
            if p > n:
                raise Exception("No divisor found for base {}".format(base))
            if n % p == 0:
                ds.append(p)
                break
    assert len(ds) == 9
    return ds

def solve(inputs):
    import itertools
    N, J = inputs
    coins = []
    for c in itertools.count(0):
        coin = to_jam_coin(c, N)
        if is_jam_coin(coin):
            coins.append(coin)
            if len(coins) == J:
                break
    solution = {}
    for coin in coins:
        print '{} {}'.format(coin, ' '.join(map(str, divisors(coin))))
    return solution

def print_outputs(solution):
    pass

if __name__ == '__main__':
    lines = read_stdin_lines()
    inputs = parse_lines(lines)[0]
    outputs = solve(inputs)
    print_outputs(outputs)
