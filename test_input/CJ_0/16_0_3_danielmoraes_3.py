import math


def new_jamcoin(size):
    return int(math.pow(2, size - 1) + 1)


def jamcoin_to_base(jamcoin, base):
    return int(jamcoin_repr(jamcoin), base)


def jamcoin_repr(jamcoin):
    return "{0:b}".format(jamcoin)


def find_divisor(value):
    for i in prime_100:
        if value % i == 0:
            return i
    return -1

prime_100 = [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
    73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151,
    157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233,
    239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317,
    331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419,
    421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503,
    509, 521, 523, 541
]

t = int(raw_input())

for i in xrange(1, t + 1):
    n, j = map(int, raw_input().split(' '))

    jamcoin = new_jamcoin(n)

    print "Case #{}:".format(i)

    k = 0
    while k < j:
        is_prime = False
        divisors = []
        for base in range(2, 11):
            divisor = find_divisor(jamcoin_to_base(jamcoin, base))
            if (divisor == -1):
                is_prime = True
                break
            else:
                divisors += [divisor]

        if not is_prime:
            print jamcoin_repr(jamcoin), " ".join(map(str, divisors))
            k += 1

        jamcoin += 2
