#! /usr/bin/env python3

import sys

NUMBER_OF_PRIMES = 100

primes = [2] 
for primep in range(3,1<<30,2):
    for p in primes:
        if primep % p == 0: break
    else:
        primes.append(primep)
        if len(primes)==NUMBER_OF_PRIMES:
            break


# For every number b=2..10 compute b**k % primes[i] for k=0..100

by_base = [None, None]

for b in range(2,11):
    res = [ [1] for p in primes ]
    for k in range(129):
        for i,r in enumerate(res):
            r.append((r[-1]*b)%primes[i])
    by_base.append(res)

### Now by_base contains:
# by_base[ base ][ prime-idx ][ power ]

def generate_coins(LEN, N):

    for bits in range(100):
        for k in range(1<<bits, 1<<(bits+1)):
            s = [0,LEN-1]
            for b in range(bits+1):
                if k & (1<<b):
                    s.append(b+1)
            divs = []
            for base in range(2,11):
                bb = by_base[base]
                for i, p in enumerate(primes):
                    S=0
                    bp = bb[i]
                    for ss in s:
                        S += bp[ss]
                    if S%p==0:
                        divs.append(p)
                        break
                else:
                    # it looks the number is pseudoprime
                    break
            else:
                yield (s,divs)
                N -= 1
                if N==0: return
    

test_cases = int(sys.stdin.readline())
for test_case in range(1, test_cases+1):
    Len, N = map(int,sys.stdin.readline().split())
    print("Case #{}:".format(test_case))
    for s, divs in generate_coins(Len,N):
        print( "{} {}".format(
            "".join(
                ('1' if x in s else '0')
                for x in range(max(s),-1,-1) ),
            " ".join(map(str,divs))))

# main

