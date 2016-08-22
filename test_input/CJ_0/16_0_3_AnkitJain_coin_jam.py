
import itertools


def is_prime(n):
    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
            return False, x

    return [True]


def get_jam_coin(n, j):
    possible_coins = ["".join(seq) for seq in itertools.product("01", repeat=n-2)]
    result = []

    for c in possible_coins:
        cj = '1%s1' % c
        all_interpretations = []
        for i in range(2, 11):
            all_interpretations.append(int(cj, i))

        divisors = []
        for intr in all_interpretations:
            x = is_prime(intr)
            if not x[0]:
                divisors.append(x[1])
            else:
                divisors = []
                break

        if divisors:
            divisors = map(str, divisors)
            result.append(cj + " " + " ".join(divisors))

        if len(result) == j:
            break

    for i in result:
        print i


T = int(raw_input())

for i in range(T):
    nj = map(int, raw_input().split(" "))
    print "Case #%s:" % str(i+1)
    get_jam_coin(nj[0], nj[1])