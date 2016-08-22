import math
from datetime import datetime

ZERO = '0'
ONE = '1'

MAX = 100000

def in_base(jamcoin, base):
    value = 0
    n = len(jamcoin)
    for i in range(0,n):
        digit = int(jamcoin[-1-i])
        value += digit * (base ** i)
    return value

def in_binary(num, size):
    str_num = "{0:b}".format(num)
    while len(str_num) < size:
        str_num = ZERO + str_num
    return str_num

def is_prime(num):
    if num % 2 == 0 and num > 2:
        return False, 2
    i = 3
    # We don't want to spend too much time checking primes
    limit = min(int(math.sqrt(num)), MAX)
    while i <= limit:
        if num % i == 0:
            return False, i
        i += 2
    return True, None

def gen_num(N):
    # Biggest binary number of size N-2
    print('HELLO')
    biggest = 2 ** (N-2) - 1
    print('biggest=%s' % biggest)

    i=0
    while i <= biggest:
        print(i)
        value = str(in_binary(i, N-2))
        i += 1
        yield ONE + value + ONE

def gen_jamcoin(J, N):
    generator = gen_num(N)
    list_jamcoins = {}
    for candidate in generator:
        print('Candidate %s' % candidate)
        list_divisors = []
        is_a_jamcoin = True
        for i in range(2,11):
            number_to_check = in_base(candidate, i)
            is_a_prime, divisor = is_prime(number_to_check)
            if is_a_prime:
                is_a_jamcoin = False
                break
            else:
                list_divisors.append(divisor)
        if is_a_jamcoin:
            list_jamcoins[candidate] = list_divisors
        if len(list_jamcoins) == J:
            break
    return list_jamcoins

f_in = open('input.txt', 'r')
f_in.readline() # We already know there's only one test

f_out = open('output.txt', 'w')
f_out.write('Case #1:\n')

N, J = map(int, f_in.readline().split(' '))
list_jamcoins = gen_jamcoin(J, N)
for jamcoin, divisors in list_jamcoins.iteritems():
    f_out.write('{} {}\n'.format(jamcoin, ' '.join(str(div) for div in divisors)))
