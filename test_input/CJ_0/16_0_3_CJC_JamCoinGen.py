import math


def factor_by(x, m, ds):
    if x % m == 0:
        if m not in ds:
            ds[m] = 1
            return m
        if x / m not in ds:
            ds[x / m] = 1
            return int(x / m)
    return 0


def is_prime(x, ds):
    fac = factor_by(x, 2, ds)
    if fac != 0:
        return fac
    fac = factor_by(x, 3, ds)
    if fac != 0:
        return fac
    sqrt = math.floor(math.sqrt(x))
    for i in range(5, sqrt, 6):
        # print(i)
        fac = factor_by(x, i, ds)
        if fac != 0:
            return fac
        fac = factor_by(x, i + 2, ds)
        if fac != 0:
            return fac
    return 0


t = int(input().strip())
for at in range(t):
    l, n = list(map(int, input().strip().split(" ")))
    mini = (2 ** (l - 1) + 1)
    maxi = (2 ** l - 1)
    count = 0
    print('Case #{0}:'.format(at + 1))
    for x in range(mini, maxi + 1, 2):
        if count == n:
            break
        out = []
        ds = {0: 1}
        bin_s = '{0:b}'.format(x)
        for base in (range(2, 11)):
            trans = int(bin_s, base)
            isJamCoin = True
            div = is_prime(trans, ds)
            if div == 0:
                isJamCoin = False
                break
            out.append(str(div))
        if isJamCoin:
            print('{0} {1}'.format(bin_s, " ".join(out)))
            count += 1
