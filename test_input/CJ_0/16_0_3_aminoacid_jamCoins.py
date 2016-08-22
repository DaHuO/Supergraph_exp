from math import sqrt
from math import floor
import itertools as it


def baseNum(j, N):
    ans = 0
    l = len(str(j))

    for ind, i in enumerate(str(j)):
        ans += pow(N, l - 1 - ind) * int(i)
    return ans


def isPrime(a):
    if a < 2:
        return False
    if a == 2 or a == 3:
        return True  # manually test 2 and 3
    if a % 2 == 0 or a % 3 == 0:
        return False  # exclude multiples of 2 and 3

    maxDivisor = a**0.5
    d, i = 5, 2
    while d <= maxDivisor:
        if a % d == 0:
            return False
        d += i
        i = 6 - i

    return True


def smallestDivisor(n):
    if n % 2 == 0:
        return 2

    else:
        squareRootOfn = int(floor(sqrt(n))) + 1
        for i in xrange(3, squareRootOfn, 2):
            if n % i == 0:
                return int(i)
                break


def jamCoins(N, J,  inp):
    gen = it.product("01", repeat=N - 2)
    count = {}

    while len(count) < J:
        num = '1' + ''.join(map(str, next(gen))) + '1'
        allNotPrime = True
        curList = []

        for base in xrange(2, 11):
            curList.append(baseNum(num, base))
            if isPrime(curList[-1]):
                allNotPrime = False

        if allNotPrime:
            legitimacy = map(lambda x: smallestDivisor(x), curList)
            count[num] = legitimacy

    print 'Case #%d:' % (inp + 1)
    for i in count:
        print i, ' '.join([str(j) for j in count[i]])


if __name__ == '__main__':
    for i in xrange(input()):
        N, J = map(int, raw_input().split())
        jamCoins(N, J, i)
