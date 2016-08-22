N = 32
J = 500

A = [2, 3, 5, 7, 11, 13, 17, 19, 23]

def powermod(a, d, n):
    if d == 0:
        return 1

    if d % 2 == 0:
        k = powermod(a, d / 2, n)
        return (k * k) % n
    return (a * powermod(a, d - 1, n)) % n

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def divisor(n):
    if n % 2 == 0:
        return 2

    s = n - 1
    while s % 2 == 0:
        s /= 2

    factors = []
    for a in A:
        temp = s
        mod = powermod(a, temp, n)
        factors.append(gcd(mod - 1, n))
        while temp != n - 1 and mod != 1 and mod != n - 1:
            mod = (mod * mod) % n
            factors.append(gcd(mod - 1, n))
            temp *= 2
        if mod != n - 1 and temp % 2 == 0:
            for factor in factors:
                if factor != 1 and factor != n:
                    return factor
    return None

def to_str(mask):
    ret = ''
    for i in xrange(N - 1, -1, -1):
        if (mask & (1 << i)) != 0:
            ret += '1'
        else:
            ret += '0'
    return ret

def to_int(mask, b):
    mult = 1
    ret = 0
    for i in xrange(N):
        if (mask & (1 << i)) != 0:
            ret += mult
        mult *= b
    return ret

print 'Case #1:'

ct = 0
for mask in xrange(1L << (N - 1), 1L << N):
    if ct == J:
        break

    if mask % 2 == 0:
        continue

    divisors = []
    prime = False
    s = to_str(mask)

    for b in xrange(2, 11):
        n = to_int(mask, b)
        k = divisor(n)
        if k is None:
            prime = True
            break
        divisors.append(k)

    if not prime:
        print '%s %s' % (s, ' '.join(map(str, divisors)))
        ct += 1
