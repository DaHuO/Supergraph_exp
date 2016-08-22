# gmpy2 can be found here: https://github.com/aleaxit/gmpy
from math import ceil, sqrt

from gmpy2 import digits, is_prime


N = 32
J = 500


def none_prime(base2str):
    for b in range(2, 11):
        n = int(base2str, base=b)
        if is_prime(n):
            return False
    return True


def find_divisors(base2str):
    for b in range(2, 11):
        n = int(base2str, base=b)
        d = 2
        while True:
            assert d <= ceil(sqrt(n))
            if n % d == 0:
                yield str(d)
                break
            d += 1
            if d > 7:
                raise RuntimeError("timeout")


def print_result(coins):
    print "Case #1:"
    for coin, divisors in coins:
        print "{} {}".format(coin, ' '.join(divisors))


def main():
    print "Case #1:"
    lower = 2 ** (N - 1) + 1
    upper = 2 ** N - 1
    coins = []
    current = upper
    while len(coins) < J:
        assert current >= lower
        base2str = digits(current, 2)
        if none_prime(base2str):
            try:
                divisors = list(find_divisors(base2str))
                coins.append((base2str, divisors))
                print "{} {}".format(base2str, ' '.join(divisors))
            except RuntimeError:
                pass
        current -= 2


if __name__ == '__main__':
    main()