def single(func):
    return func(raw_input())

def row(func):
    return map(func, raw_input().split())

def printcase(case, out, pattern='Case #%d: %s'):
    print pattern % (case, out)

def repeat(func, times):
    return [func() for _ in xrange(times)]

with open('primes.txt') as f:
    primes = map(int, f.read().split())

def firstdiv(val):
    for p in primes:
        if p < val and val % p == 0:
            return p

printcase(1, '')

T = single(int)
for t in xrange(1, T + 1):
    N, J = row(int)
    start = int('1%s1' % ('0'*(N-2)), 2)
    stop = int('1'*N, 2)
    found = 0

    for x in xrange(start, stop+1, 2):
        #print x
        binval = bin(x)[2:]
        divisors = []
        for base in xrange(2, 11):
            val = int(binval, base)
            #print base, val
            divisor = firstdiv(val)
            if not divisor: break
            divisors.append(divisor)
        else:
            assert len(divisors) == 9
            print binval, ' '.join(map(str, divisors))
            found += 1
            if found == J: break
