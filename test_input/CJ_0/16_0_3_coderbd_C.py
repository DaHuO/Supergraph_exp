#!/usr/bin/python

def get_prime_list(n):
    m = n + 1
    a = range(m)
    a[1], sn = 0, int(round(n ** 0.5)) + 1
    for i in xrange(2, sn):
        if a[i]:
            a[i*i: m: i] = [0] * len(xrange(i*i, m, i))
    return filter(None, a)

def get_divisor(primes, num):
    for prime in primes:
        if prime * prime > num:
            return None
        if num % prime == 0:
            return prime
    return None

t = int(raw_input())
n, j = map(int, raw_input().split())

count, m = 0, 2 ** (n-2)
primes = get_prime_list(2**20)

print 'Case #1:'
for num in xrange(m):
    if count == j: break
    coin = 2 ** (n-1) + 2 * num + 1
    coin_bin = '{0:b}'.format(coin)
    div = [get_divisor(primes, int(coin_bin, b)) for b in xrange(2, 11)]
    if None not in div:
        count += 1
        print coin_bin, ' '.join(map(str, div))
        