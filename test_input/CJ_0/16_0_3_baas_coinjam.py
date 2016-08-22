import sys
import itertools

def is_prime(num):
    if num % 2 == 0 or num % 3 == 0:
        return False

    for i in range(4, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True

def real_jamtest(jamstr):
    for base in range(2, 11):
        num = int(jamstr, base)
        if is_prime(num):
            return False

    return True

def is_jamcoin(jamstr):
    if jamstr[0] != '1' or jamstr[-1] != '1':
        return False

    return real_jamtest(jamstr)

def solve(jamcoin_len, num_jamcoins):
    jamcoins = list()
    for p in itertools.product('10', repeat=jamcoin_len):
        s = ''.join(p)
        if is_jamcoin(s):
            jamcoins.append(s)
        if len(jamcoins) == num_jamcoins:
            break

    return jamcoins

def get_divisors(num, divs_so_far):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0 and i not in divs_so_far:
            divs_so_far.append(i)
            break

l = sys.stdin.readlines()
relevant_line = l[1].strip()
(n, j) = relevant_line.split(' ')
jamcoin_len = int(n)
num_jamcoins = int(j)

jamcoins = solve(jamcoin_len, num_jamcoins)

for jamcoin in jamcoins:
    divisors = list()
    for i in range(2, 11):
        get_divisors(int(jamcoin, i), divisors)
    print "{} {}".format(jamcoin, ' '.join([str(div) for div in divisors]))
    

