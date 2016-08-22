from time import time
import math


def get_devider(number):
    if number % 2 == 0 and number > 2:
        return 2
    dv = 3
    n = time()
    while dv < int(math.sqrt(number)) + 1:
        if number % dv == 0:
            return dv
        dv += 2
        if time() - n > 0.8:
            return None
    return None


def print_solutions(filename):
    content = open(filename).read().strip().split('\n')
    test_case_count = int(content[0])
    i = 1
    while i <= test_case_count:
        print("Case #%s:" % (i, ))
        n, j = [int(m) for m in content[i].split(' ')]
        jamcoin = '1%s1' % ('0' * (n - 2))
        jamcoin_int = int(jamcoin, 2)
        found = 0
        while found < j:
            divisors = []
            for base in xrange(2, 11):
                cn = int(jamcoin, base)
                d = get_devider(cn)
                if d:
                    divisors.append(str(d))
                else:
                    break
            if len(divisors) == 9:
                print("%s %s" % (jamcoin, " ".join(divisors)))
                found += 1
            jamcoin_int += 2
            jamcoin = bin(jamcoin_int)[2:]

        i += 1

filename = raw_input()
print_solutions(filename)
