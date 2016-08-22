import math
import itertools


def dividor(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if divmod(n, i)[1] == 0:
            return i


def is_coinjam(coinjam):
    divs = []
    for k in range(2, 11):
        n = int(coinjam, k)
        d = dividor(n)

        if d is None:
            return None

        divs.append(d)

    return divs


def solve_jamcoin(n, j):
    coins = itertools.product('01', repeat=n - 2)

    coins_rv = []
    for lst in coins:
        lst = ('1', ) + lst + ('1', )
        if len(coins_rv) == j:
            break

        coinjam = ''.join(lst)
        rv = is_coinjam(coinjam)
        if rv:
            coins_rv.append(coinjam + ' ' + ' '.join(map(str, rv)))

    return '\n'.join(map(str, coins_rv))


nb_cases = int(input())
for i in range(nb_cases):

    n, j = map(int, raw_input().split(' '))
    rv = solve_jamcoin(n, j)

    print("Case #{}:\n{}".format(i + 1, rv))
