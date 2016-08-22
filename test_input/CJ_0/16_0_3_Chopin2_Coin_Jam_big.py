import sys
import math
import random

import numpy

highest = int(math.ceil(int('1'*16))**0.5+1)

def primesfrom3to(n):
    """ Returns a array of primes, 3 <= p < n """
    sieve = numpy.ones(n/2, dtype=numpy.bool)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = False
    return 2*numpy.nonzero(sieve)[0][1::]+1

list_of_primes = primesfrom3to(highest)


def possible_jamcoin(N):
    num = ['1']
    for i in (range(1,N-1)):
        num.append(str(random.randint(0,1)))
    num.append('1')
    num =  int(''.join(num))
    return num


def generating_the_jamcoins(N,J):
    with open('Big.Out', 'w') as f:
        f.write('Case #1:'+ '\n')
        list_of_jamcoins = []
        count = 0
        i = 0
        while count < J:
            list_of_jamcoins_and_Ks = []
            num = possible_jamcoin(N)
            while num in list_of_jamcoins:
                num = possible_jamcoin(N)
            while is_it_jamcoin(num) == False:
                num = possible_jamcoin(N)
                while num in list_of_jamcoins:
                    num = possible_jamcoin(N)
            list_of_jamcoins_and_Ks.append(num)
            list_of_jamcoins_and_Ks.extend(is_it_jamcoin(num)['K'])
            f.write(' '.join([str(i) for i in list_of_jamcoins_and_Ks]) + '\n')
            list_of_jamcoins.append(num)
            count += 1

def is_it_jamcoin(number):
    K = []
    for i in converting_to_different_base(number):
        num = is_prime(i)
        if num == True:
            return False
        else:
            K.append(num['K'])
    return {'is_jamcoin': True, 'K' : K}


def is_prime(n):
    for i in list_of_primes:
        if i >= n:
            return True
        if n % i == 0:
            return {'is_prime': False, 'K' : i}
    return True

def converting_to_different_base(number):
    in_different_bases = []
    for i in range(9):
        in_different_bases.append(int(str(number),i+2))
    return in_different_bases
   


def main():
    generating_the_jamcoins(32,500)
if __name__ == '__main__':
    main()

