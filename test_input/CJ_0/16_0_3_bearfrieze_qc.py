import fileinput
from math import sqrt
from itertools import count, islice
from time import sleep

# http://stackoverflow.com/a/27946768/5964259
def prime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

def solved(coin):
    return all(not prime(int(coin, base)) for base in range(2, 11))

def divisor(n):
    for i in range(2, n):
        if n % i == 0: return i

def divisors(coin):
    return ' '.join([str(divisor(int(coin, base))) for base in range(2, 11)])

def solve(N, J):
    i = 0
    fix = '{0:0%db}' % (N - 2)
    solutions = []
    while len(solutions) < J:
        coin = '1' + fix.format(i) + '1'
        if solved(coin):
            print(coin)
            solutions.append(coin + ' ' + divisors(coin))
        i += 1
    return '\n'.join(solutions)

f = fileinput.input()
T = int(f.readline())

for case in range(1, T + 1):
    N, J = [int(s) for s in f.readline().strip('\n').split(' ')]
    print('Case #%d:\n%s' % (case, solve(N, J)))
