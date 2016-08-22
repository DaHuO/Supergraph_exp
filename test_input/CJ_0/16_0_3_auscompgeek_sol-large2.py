#!/usr/bin/env python3

from itertools import product


def get_factor(k, trials=2000):
    if k & 1 is 0:
        return 2
    if k % 3 is 0:
        return 3
    i = 5
    t = int(k**.5)
    while i <= t and trials:
        if k % i is 0:
            return i
        i += 2
        if k % i is 0:
            return i
        i += 4
        trials -= 1


def get_proof(x):
    factors = []

    for b in range(2, 11):
        k = int(x, b)
        f = get_factor(k)
        if not f:
            break
        factors.append(f)

    else:
        return factors


def solve(N, J):
    count = 0
    for p in product('01', repeat=N-2):
        x = '1%s1' % ''.join(p)
        factors = get_proof(x)
        if factors:
            print(x, *factors)
            count += 1
            if count is J:
                break


def main():
    assert int(input()) is 1
    print('Case #1:')
    N, J = map(int, input().split())
    solve(N, J)


if __name__ == "__main__":
    main()
