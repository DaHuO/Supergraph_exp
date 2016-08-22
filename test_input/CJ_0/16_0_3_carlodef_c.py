import math
import itertools


def proper_divisor(n):
    for i in xrange(2, int(math.log(n)) + 1):
        if (n % i) == 0:
            return i


def check_jamcoin(x, N):
    out = []
    for b in xrange(2, 11):
        n = sum([b ** (N-1-i) for i in itertools.compress(xrange(1, N), x)], b ** (N-1) + 1)
        d = proper_divisor(n)
        if d:
            out.append(d)
        else:
            return False
    return out


if __name__ == '__main__':
    raw_input()
    N, J = map(int, raw_input().split())
    print "Case #1:"
    nb_of_jamcoins_found = 0
    for x in itertools.product([0, 1], repeat=N-2):
        divisors = check_jamcoin(x, N)
        if divisors:
            print '1%s1' % ''.join(str(a) for a in x),
            for d in divisors:
                print d, 
            print
            nb_of_jamcoins_found += 1
        if nb_of_jamcoins_found >= J:
            break
