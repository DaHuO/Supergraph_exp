import math


def JamCoins(N, J):
    coinCandidate = '1' + '0' * (N-2) + '1'
    for i in range(0, J):
        coinCandidate, coin, divisors = JamCoin(coinCandidate)
        print coin,
        for d in divisors:
            print ' ', d,
        print '\n',


def JamCoin(coinCandidate):
    divisors = [0] * 9
    while divisors[8] == 0:
        coin = coinCandidate
        for b in range(2, 11):
            n = int(coinCandidate, b)
            d = Divisor(n)
            if d != 0:
                divisors[b - 2] = d
            else:
                break
        coinCandidate = bin(int(coinCandidate, 2) + 2)[2:]
    return coinCandidate, coin, divisors


def Divisor(n):
    for i in range(2, 1000000):
        if n % i == 0:
            return i
    return 0


JamCoins(32, 500)
