import math
import os
import sys

from functools import reduce
from itertools import product


def non_prime(n):
    if n == 2:
        return False
    if n == 3:
        return False
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return i

        i += w
        w = 6 - w

    return False


def next_conf(N):
    for p in product("01", repeat=N-2):
        yield list(map(int, p))


def task(N, J):
    base = [1 + math.pow(x, N - 1) for x in range(2, 11)]
    result, cache = dict(), []
    for p in next_conf(N):
        if p in cache:
            continue
        cache.append(p)
        config = ''.join(list(map(str, p)))
        divisors = []
        additive = [reduce(lambda x, y: x + y, [h * pow(b, N - 2 - i) for i, h in enumerate(p)], 0) for b in range(2, 11)]
        for i, x in enumerate(base):
            dvsor = non_prime(x + additive[i])
            if not dvsor:
                break
            divisors.append(dvsor)
        else:
            result[config] = divisors
            if len(result.keys()) == J:
                break
    res_str = ''
    for k in result:
        res_str += '1%s1 %s' % (str(k), ' '.join(list(map(str, result[k]))) + '\n')
    return res_str


def main():
    with open(sys.argv[1], 'r') as f:
        src = f.read()

    lines = src.splitlines()

    T, res = int(lines[0]), ''
    for i in range(1, T + 1):
        res += 'Case #%d:\n%s\n' % (i, task(*(map(int, lines[i].split(' ')))))

    with open(os.path.splitext(sys.argv[1])[0] + '.out', 'w') as f:
        f.write(res)

if __name__ == '__main__':
    main()
