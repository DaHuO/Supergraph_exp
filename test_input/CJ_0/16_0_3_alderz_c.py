def toBase(base, n):
    ss = bin(n)[2:]
    l = len(ss) - 1
    i = 0
    x = 0
    while i <= l:
        d = int(ss[i]) * (base ** (l - i))
        x += d
        i += 1
    return x

def getFactor(primes, n):
    for i in primes:
        if i == n:
            return -1
        if n % i == 0: 
            return i
    return -1

def find(primes, r):
    count = 0
    for n in r:
        if n % 2 == 0:
            continue
        found = True
        factors = [0] * 11
        for i in range(2, 11):
            f = getFactor(primes, toBase(i, n))
            if f != -1:
                factors[i] = f
            else:
                found = False
                break
        if found:
            print(bin(n)[2:], end="")
            for k in factors[2:]:
                print(" " + str(k), end="")
            print("")
            count += 1
            if count == 501:
                break
