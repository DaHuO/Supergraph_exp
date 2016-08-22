import sys
import pyprimes
import pyprimes.probabilistic
import pyprimes.factors

p = pyprimes.primes()
primes_list = [next(p) for x in range(10000000)]
max_list_prime = primes_list[-1]

def getFactor(val):
    for pnum in primes_list:
        if val % pnum == 0:
            return pnum
    #print('This is too hard, skipping.')
    return 0

    """
    next_p = pyprimes.next_prime(max_list_prime)

    while val % next_p != 0:
        next_p = pyprimes.next_prime(next_p)

    return next_p
    """

def convertToBase(coin, b):
    coin_s = '{0:b}'.format(coin)
    # print(coin_s)
    val = 0
    for i in range(0, len(coin_s)):
        if coin_s[i] == '1':
            # print('b = {}, i = {}'.format(b, i))
            val += pow(b, len(coin_s) - 1 - i)
    return val

input()
n, j = map(int, input().split(" "))

print("Case #1:")

coin = pow(2, n-1) + 1
lim = pow(2, n)

validCoins = 0
ctr = 0

p = pyprimes.probabilistic.IsProbablePrime()

while coin < lim and validCoins < j:
    ctr += 1
    #print('Iteration {}'.format(ctr))

    out = ['{0:b}'.format(coin)]
    for b in range(2, 11):
        bVal = convertToBase(coin, b)
        #print('Testing primality of {}'.format(bVal))
        if p._randomized_miller_rabin(bVal) != 0:
            break
        else:
            #factor = next(pyprimes.factors.factors(bVal))[0]
            factor = getFactor(bVal)
            if factor == 0:
                break
            #print('{} is divisor of {}'.format(factor, bVal))
            out.append(factor)

    coin += 2
    if len(out) == 10:
        validCoins += 1
        print(' '.join(map(str, out)))
