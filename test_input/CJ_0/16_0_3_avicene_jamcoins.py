# from __future__ import print_function
from array import array
import math
import itertools

__author__ = 'adilmezghouti'

def is_prime(n):
    # print "--------------"
    # print n
    # print "--------------"
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))


def factors(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i
    # return set(reduce(list.__add__,
    #             ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
# print [0]*3
# print int("101",2)
# print int("101",3)
# print int("100001",2)
# print(increment_binary('100001'))

template = "1x1"
def generate(jamcoin_length, number_of_cases):
    jamcoin_core = ['0']*(jamcoin_length-2)
    jamcoin = template.replace("x", "".join(jamcoin_core))
    jamcoin_bases = []
    counter = 0


    divisors = []
    for x in map(''.join, itertools.product('01', repeat=jamcoin_length - 2)):
        jamcoin = template.replace("x", x)
        jamcoin_bases = []
        is_any_prime = False

        for base in range(2,10+1):
            jamcoin_bases.append(int(jamcoin, base))
            if is_prime(int(jamcoin, base)):
                is_any_prime = True
                break

        # is_any_prime = filter(lambda x: is_prime(x), jamcoin_bases)
        # print len(is_any_prime)

        if not is_any_prime:
            # print "find a divisor"
            for coin in jamcoin_bases:
                divisors.append(str(factors(coin)))
        if len(divisors) == 9:
            print jamcoin + ' ' + ' '.join(divisors)
            # print divisors
            counter += 1
            divisors = []
        if counter > number_of_cases - 1:
            break

print "Case #1:"
# generate(16,50)
generate(16,50)

# print factors(1234523)
# print list(factors(1234523))[1]