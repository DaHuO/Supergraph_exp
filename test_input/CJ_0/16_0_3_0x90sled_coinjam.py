import fileinput
import itertools
import math


def jamcoin_generator(length):
    # Standard code for determining prime-ness
    def is_prime(n):
        if n % 2 == 0 and n > 2:
            return False
        return all(n % i for i in range(3, long(math.sqrt(n)) + 1, 2))

    # Remove 2 from the length because jamcoins always start and end with 1
    for i in itertools.product([0, 1], repeat=length - 2):
        coin = ''.join(map(str, (1,) + i + (1,)))
        if not any(map(lambda x: is_prime(long(coin, x)), range(2, 11))):
            yield coin


def get_divisors(N, rmin=2, rmax=11):
    divisors = list()
    for base in range(rmin, rmax):
        num = long(N, base)
        i = 2
        while True:
            if num % i == 0:
                divisors.append(num / i)
                break
            i += 1
    return divisors


def main():
    length, coins = [line.strip() for line in fileinput.input()][1:].pop().split()

    gen = jamcoin_generator(long(length))
    print "Case #1:"
    for case in range(1, long(coins) + 1):
        coin = next(gen)
        print coin, ' '.join(map(str, get_divisors(coin)))


if __name__ == '__main__':
    main()
