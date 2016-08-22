from redef_io import *

from math import sqrt


def get_factor(x):
    for f in xrange(2, int(sqrt(x)) + 1):
        if x % f == 0:
            return f
    return -1


def str_base(number, base=2):
    """
    Inspired from http://stackoverflow.com/a/24763277/4038191
    """
    (d, m) = divmod(number, base)
    if d > 0:
        return str_base(d, base) + str(m)
    return str(m)


def get_sequence(i):
    l = n - 2

    return list(str_base(i).rjust(l, '0'))


def validate_jamcoin(coin=''):
    """
    If coin is a valid jamcoin, returns the list of nontrivial divisors. Else returns None.
    """
    divisors = []
    for base in xrange(2, 11):
        factor = get_factor(int(coin, base))
        if factor == -1:
            return None
        divisors.append(factor)
    return divisors


def generate_jamcoins():
    """
    Generates j jamcoins of length n along with their nontrivial divisors.
    """
    global n, j
    # Number of jamcoins created
    c = 0
    # Loop iteration number
    idx = 0

    jamcoins = []

    while c < j:
        jamcoin = ''.join(['1'] + get_sequence(idx) + ['1'])
        idx += 1

        divisors = validate_jamcoin(jamcoin)

        if divisors is None:
            continue

        jamcoins.append(' '.join([jamcoin] + [str(d) for d in divisors]))
        c += 1

    return jamcoins


t = int(raw_input())

for it in xrange(t):
    line = raw_input().split(' ')
    n = int(line[0])
    j = int(line[1])

    print_file('\n' + '\n'.join(generate_jamcoins()))
