from itertools import product


def suspect(b, t, u, n):
    prod = 1
    while u:
        if u & 1:
            prod = (prod*b) % n
        b = (b * b) % n
        u //= 2
    if prod == 1:
        return True
    for i in range(1, t + 1):
        if prod == n-1:
            return True
        prod = (prod * prod) % n
    return False


def isprime(n):
    k = n - 1
    t = 0
    while not (k % 2 == 0):
        t += 1
        k //= 2
    for m in [2, 3, 5, 7]:
        if n > m and n % m == 0:
            return False
    if suspect(61, t, k, n) and suspect(7, t, k, n) and suspect(2, t, k, n):
        return True
    return False


def divisor(x):
    for p in primes:
        if x > p and x % p == 0:
            return p
    return None

if __name__ == "__main__":
    prime = [True for _ in range(10 ** 6 + 1)]
    prime[0] = False
    prime[1] = False
    primes = list()
    for i in range(2, len(prime)):
        if not prime[i]:
            continue
        primes.append(i)
        for j in range(i + i, len(prime), i):
            prime[j] = False
    for t in range(int(input())):
        n, j = map(int, input().split())
        ret = 0
        print("Case #%d:" % (t+1))
        for p in product("01", repeat=n-2):
            x = "1" + "".join(p) + "1"
            tmp = []
            for b in range(2, 11):
                c = int(x, b)
                if isprime(c):
                    tmp = []
                    break
                d = divisor(c)
                if not d:
                    tmp = []
                    break
                tmp.append(d)
            if tmp:
                ret += 1
                print(x, " ".join(map(str, tmp)))
            if ret == j:
                break
