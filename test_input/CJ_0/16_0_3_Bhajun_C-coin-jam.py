#!/usr/bin/env python

from __future__ import division, print_function
import sys


def generate_primes(n):
    if n == 2:
        return [2]
    elif n < 2:
        return []
    
    sieve = list(range(3, n + 1, 2))
    root_n = n**0.5
    mid = (n + 1) // 2 - 1
    i = 0
    m = 3
    
    while m <= root_n:
        if sieve[i]:
            j = (m * m - 3) // 2
            sieve[j] = 0
            while j < mid:
                sieve[j] = 0
                j += m
        
        i += 1
        m = 2 * i + 3
    
    return [2] + [p for p in sieve if p]

def get_factor(n, primes):
    for p in primes:
        if n % p == 0:
            return p
    return -1


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    primes = generate_primes(1000)
    
    for i in range(T):
        N, J = list(map(int, sys.stdin.readline().split()))
        
        a, b = (1 << (N - 1)) + 1, (1 << N)
        count = 0
        
        print('Case #%d:' % (i + 1))
        
        for n in range(a, b, 2):
            s = bin(n)[2:]
            bases = [int(s, j) for j in range(2, 11)]
            factors = [get_factor(x, primes) for x in bases]
            
            if all(x > -1 for x in factors):
                print(s, ' '.join(map(str, factors)))
                count += 1
            
            if count == J:
                break