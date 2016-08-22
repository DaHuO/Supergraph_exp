#!/usr/bin/env python

import itertools

def primes_up_to(order):
    """Return a list of primes up to 10^order."""
    M = 10**order
    composites = set()
    primes = set()
    for i in range(2, M):
        if i in composites: # dont sieve composites
            continue
        primes.add(i)
        cur = i+i
        for cur in range(i+i, M, i):
            composites.add(cur)
    return primes

def coin_value_from_base(base, coin):
    """Return coin value in base."""
    value = 0
    multiplier = 1
    for i, v in reversed(list(enumerate(coin))):
        if v:
            value += multiplier
        multiplier *= base
    return value

def check_base(base, coin, primes):
    """Return divisor in base or False if prime or if it or exhausts the primes
    we have precomputed, this will miss some composites, but maybes that's ok.
    """
    value = coin_value_from_base(base, coin)
    if value in primes:
        return False
    for prime in primes:
        if value % prime == 0:
            return prime
    return False

def coins_iter(N):
    """Return an iterables of jamcoins length N."""
    for inner_coin in itertools.product([False, True], repeat=(N-2)):
        yield [True] + list(inner_coin) + [True]

def print_coin(coin):
    return ''.join(map(str,map(int, coin)))

def print_coins(N, J):
    """Prints J jamcoins of length N each followed by 9 non trivial divisors."""
    primes = primes_up_to(5)
    count = 0
    for coin in coins_iter(N):
        out = []
        for base in range(2, 11):
            divisor = check_base(base, coin, primes)
            if divisor:
                out.append(divisor)
            else:
                break
        if len(out) == 9:
            print '%s %s' % (print_coin(coin), ' '.join(map(str, out)))
            count += 1
            if count == J:
                return

def main():
    T = int(raw_input())
    for i in range(T):
        print 'Case #%s:' % (i+1)
        print_coins(*map(int, raw_input().split()))


if __name__ == "__main__":
    main()
