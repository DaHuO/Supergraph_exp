import random
import sys

primes = [2, 3, 5, 7]

def go(jamcoin):
    divs = []
    for b in range(2,11):
        n = int(jamcoin, base=b)
        for prime in primes:
            if n % prime == 0:
                divs.append(prime)
                break
        else:
            return []
    return divs

def solve(N,J):
    jamcoin = '1' + '0' * (N - 2) + '1'
    jamcoins = {}
    while len(jamcoins) < J:
        if jamcoin not in jamcoins:
            res = go(jamcoin)
            if res: jamcoins[jamcoin] = res
        ind = random.randint(1,N-2)
        d = random.choice(('0','1'))
        jamcoin = jamcoin[:ind] + d + jamcoin[ind+1:]
    return jamcoins

if __name__ == '__main__':
    T = int(input())
    N, J = map(int,sys.stdin.readline().split())
    print("Case #1:")
    for jamcoin, divs in solve(N,J).items():
        print("{} {}".format(jamcoin, ' '.join(str(div) for div in divs)))
