"""

"""

import sys, operator


# from the mighty internet...
def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        #print '\t',f
        if n % f == 0:
            return False
        if n % (f+2) == 0:
            return False
        f += 6
    return True


def to_base(a, b, N):

    return reduce(operator.add, [b**n for n in range(N) if (a & (0x1 << n)) != 0], 0)


def non_trivial_divisor(n):

    print n
    d = 2
    while d < (n / 2 + 1):
        if n % d == 0:
            return d
        d += 1

    raise ValueError('stooopid!')


if __name__ == '__main__':

    with open(sys.argv[1], 'r') as f:

        n_test_cases = int(f.readline())
        test_cases = []

        for i in range(n_test_cases):
            test_cases.append(tuple(map(int, f.readline().split(' '))))

    solutions = []
    for N, J in test_cases:
        k = 0
        n = 2**(N - 1) + 1
        while k < J:
            if not any([is_prime(a) for a in [to_base(n, b, N) for b in range(2,11)]]):
                jamcoin = ''.join([('1' if (n & 0x1 << (N - i - 1)) != 0 else '0') for i in range(N)])
                #base_watermark = non_trivial_divisor(to_base(n, 2, N))
                #watermarks = [to_base(base_watermark, b, N) for b in range(2,11)]
                watermarks = [non_trivial_divisor(a) for a in [to_base(n, b, N) for b in range(2,11)]]
                print watermarks
                solutions.append((jamcoin, watermarks))
                k += 1
            n += 2

    with open('jamcoins-small.txt', 'w') as f:
        n = 1
        s_lst = ["Case #1:"]
        for solution in solutions:
            jamcoin, watermarks = solution
            s_lst.append("%s %s" % (jamcoin, ' '.join(map(str, watermarks))))
            n += 1

        f.write('\n'.join(s_lst))
