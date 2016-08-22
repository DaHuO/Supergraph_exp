import random
from gmpy2 import is_prime, gcd

def pollard(n, max_steps=10000):
    if(n%2==0):
        return 2;
    x=random.randrange(2,1000000)
    c=random.randrange(2,1000000)
    y=x
    d=1
    count = 0
    while d==1:
        count += 1
        if count > max_steps:
            return 0
        x=(x*x+c)%n
        y=(y*y+c)%n
        y=(y*y+c)%n
        d=gcd(x-y,n)
        if(d==n):
            break
    return d


def jamcoin_witn(bin_str):

    res = []
    for base in range(2, 10+1):
        n = int('1' + ''.join(bin_str) + '1', base=base)
        if is_prime(n):
            return False
        else:
            fct = pollard(n)
            if fct:
                res.append(fct)
    return res

from random import choice

def rnd_jamcoin(N):
    return [choice('01') for _ in range(N)]

def J_jamcoins(N, J):
    found = []

    while len(found) < J:
        rj = rnd_jamcoin(N-2)
        jw = jamcoin_witn(rj)
        if jw:
            found.append(('1' + ''.join(rj) + '1', jw))
            res = [found[-1][0]] + [int(x) for x in found[-1][1]]
            print(' '.join(str(x) for x in res))
    return found

print("Case # 1:")
J_jamcoins(16, 50)


