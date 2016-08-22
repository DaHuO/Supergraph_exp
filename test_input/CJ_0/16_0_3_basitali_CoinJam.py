from itertools import product
import math

primes = [3, 5, 7, 11, 13]

def divisor(n):
    if n in primes: return False
    if n%2 == 0: return 2
    if n%3 == 0: return 3

    r = int(n**0.5)
    f = 5

    while f <= r:
        if n%f == 0: return f
        if n%(f+2) == 0: return f + 2
        f += 6
        if f > 99999:
            return "SKIP"

    primes.append(n)
    return False

def generate(n, j):
    count = 0
    skipped = []
    for coin in product("01", repeat=n-2):
        coin = "1" + "".join(coin) + "1"
        divisors = []

        for i in range(2, 11):
            num = int(coin, i)
            d = divisor(num)
            if d == "SKIP":
                skipped.append(num) #{num: num, i: i, divisors:divisors})
                # print skipped
                break
            elif d:
                divisors.append(str(d))
            else:
                break

        if len(divisors) == 9:
            yield coin, divisors
            count += 1
            if count == j:
                break

if __name__ == '__main__':
    case = 'C-large'
    inp = open('%s.in'%case);
    out = open('%s.out'%case, 'w');

    cases = int(inp.readline())
    for i in xrange(1, cases + 1):
        n, j = [int(c) for c in inp.readline().split()]
        o = "Case #%d:\n"%i
        out.write(o)
        j_index = 1
        for coin, divisors in generate(n, j):
            res = '%s %s'%(coin, " ".join(divisors))
            print res
            out.write(res)
            if j_index < j:
                out.write('\n')
                j_index += 1
