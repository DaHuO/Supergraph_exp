#!/usr/bin/env python3
import sys
import multiprocessing
from math import sqrt
from collections import namedtuple
from functools import partial

prime_pair = namedtuple('prime_pair', ['is_prime', 'divisor'])
count = multiprocessing.Value('i', 0)

# max divisor value to test in is_prime
MAX_DIVISOR = 5000

def recompose(function, times):
    """Composes a function with itself multiple times.

    :param function: Function to compose
    :param times: Amount of compositions, must be greater than zero
    """
    if times <= 0:
        raise ValueError('times must be greater than zero')

    # Function to return
    def recomposed(*args, **kwargs):
        res = function(*args, **kwargs)
        for i in range(1, times):
            res = function(res)
        return res
            
    return recomposed

# TODO: probabilistic primality testing would be nice since there are way more jamcoins
#       than we need. Instead, we just cap the divisor
def is_prime(x):
    """Checks whether a natural number is prime and potentially returns a nontrivial divisor.
    """
    if x != 2 and x % 2 == 0: # even numbers 
        return prime_pair(False, 2)
    elif x < 2: # 0, 1
        return prime_pair(False, 1)
    elif x < 4: # 2, 3
        return prime_pair(True, None)
    else:
        limit = min(MAX_DIVISOR, int(sqrt(x) + 1))
        divisor = next((d for d in range(3, limit, 2) if x % d == 0), None)
        return prime_pair(divisor is None, divisor)

def jamcoin_string_generator(n, start=0, increment=1):
    """Generates all the possible jamcoin strings of a given length.

    :param n: length of the jamcoins
    :param start: index of the jamcoin to start with (default 0)
    :param increment: distance between two consecutive generated jamcoins (default 1)
    """
    # Helper functions
    increment_coin = lambda s: bin(int(s, 2) + 0b10)[2:]
    next_coin = increment_coin if increment == 1 else recompose(increment_coin, increment)

    s = '1' + '0'*(n - 2) + '1'
    if start > 0:
        s = recompose(increment_coin, start)(s)

    # Leftmost digit overflowing signals the end of the sequence
    while len(s) == n:
        yield s
        s = next_coin(s)

# Crashing this market with no survivors
def mine(amount, gen_data):
    res = []

    for s in jamcoin_string_generator(gen_data['n'], gen_data['start'], gen_data['increment']):
        base_nums = [ int(s, base) for base in range(2, 11) ]
        prime_data = [ is_prime(x) for x in base_nums ]

        # Jamcoins need to be composite on every base representation from 2 to 10
        if any(pp.is_prime for pp in prime_data):
            continue

        # Add a new jamcoin along their divisors
        res.append((s, [ pp.divisor for pp in prime_data ]))

        with count.get_lock():
            count.value += 1
        if amount is not None and count.value >= amount:
            break

    return res

if __name__ == '__main__':
    _, n, j = list(map(int, sys.stdin.read().split()))

    # I'm never parallelizing anything in python again
    NUM_PROCESSES = 8
    gen_dicts = [ { 'n': n, 'start': i, 'increment': NUM_PROCESSES } for i in range(NUM_PROCESSES) ]

    pool = multiprocessing.Pool(processes=NUM_PROCESSES)
    pool_returns = pool.map(partial(mine, j), gen_dicts)
    jamcoins = [ jamcoin for sublist in pool_returns for jamcoin in sublist ]

    print("Case #1:")
    for jamcoin, divisors in sorted(jamcoins[:j], key=lambda pair: pair[0]):
        print("{} {}".format(jamcoin, ' '.join(map(str, divisors))))
