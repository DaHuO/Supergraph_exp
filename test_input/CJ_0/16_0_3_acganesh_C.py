from math import sqrt
import random
from itertools import product

from time import sleep

def jamcoins(N, J):
    print 'Case #1:'
    count = 0
    for x in product([0, 1], repeat=N-2):
        cand = ''.join(map(str, x))
        cand = int('1'+cand+'1')
        if is_valid(cand):
            timeout = False
            s = str(cand)

            for b in xrange(2, 11):
                f = get_factor(to_base(cand, b))
                if f:
                    s += ' '+str(f)
                else:
                    timeout = True
                    break
            if not timeout:
                count += 1
                print s
        if count == J:
            break


def to_base(N, b):
    s = str(N)
    total = 0
    for i, d in enumerate(reversed(s)):
        i = int(i); d = int(d)
        total += d*b**i
    return total

def get_factor(N, limit=1000):
    for x in xrange(2, limit):
        if N % x == 0:
            return x
    return None

def is_valid(N):
    for b in xrange(2, 11):
        if miller_rabin(to_base(N, b)): return False
    return True


# From Euler library
def miller_rabin(n):
    """
    Check n for primality:  Example:

    >miller_rabin(162259276829213363391578010288127)    #Mersenne prime #11
    True

    Algorithm & Python source:

    http://en.literateprograms.org/Miller-Rabin_primality_test_(Python)

    """
    d = n - 1
    s = 0
    while d % 2 == 0:
        d >>= 1
        s += 1
    for repeat in range(20):
        a = 0
        while a == 0:
            a = random.randrange(n)
        if not miller_rabin_pass(a, s, d, n):
            return False
    return True

def miller_rabin_pass(a, s, d, n):
    a_to_power = pow(a, d, n)
    if a_to_power == 1:
        return True
    for i in range(s-1):
        if a_to_power == n - 1:
            return True
        a_to_power = (a_to_power * a_to_power) % n
    return a_to_power == n - 1

def validate():
    assert is_valid(100011)
    assert is_valid(111111)
    assert is_valid(111001)
    print 'Tests passed!'

jamcoins(32, 500)
