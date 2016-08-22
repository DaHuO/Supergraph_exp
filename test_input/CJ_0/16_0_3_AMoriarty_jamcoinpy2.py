# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 17:33:44 2016

@author: alex
"""
import sys
import numpy
import math


def small_sieve_primes(n):

    # Find all primes n > prime > 2 using the Sieve of Eratosthenes 
    # For efficiency, track only odd numbers (evens are nonprime)

    sieve = numpy.ones(n/2, dtype=numpy.bool) 
    limit = int(math.sqrt(n)) + 1 
    
    for i in range(3, limit, 2): 
        if sieve[i/2]:
            sieve[i*i/2 :: i] = False
            
    prime_indexes = numpy.nonzero(sieve)[0][1::]
    primes  = 2 * prime_indexes.astype(numpy.int32) + 1 
    return set(primes), primes

def get_low_high(L):
    low, high = "", ""
    for i in xrange(L):
        if i == 0 or i == L-1:
            low+="1"
            high+="1"
        else:
            low+="0"
            high+="1"
    return low, high

def ntd(N):
    for i in primes_npy[0:100000]:
        if N%i == 0:
            return i
    #for i in xrange(3,N//2 + 1,2):
    #    if N%i == 0:
    #        return i


### SMALL lowest:
## int("1000000000000001",2)
## Out[60]: 32769
### SMALL highest: 
## int("1111111111111111",2)
## Out[61]: 65535



"""
Input 
 	 
1
6 3

Output 

Case #1:
100011 5 13 147 31 43 1121 73 77 629
111111 21 26 105 1302 217 1032 513 13286 10101
111001 3 88 5 1938 7 208 3 20 11

100011 5 13 3 31 43 3 73 7 3
101101 3 5 5 3 7 5 3 5 7
110001 7 5 3 11 43 3 5 7 3
"""
c = 0

def main(T, L,J):
    global primes, primes_npy
    global c
    
    print("Case #%d:"%T)
    bases = [2,3,4,5,6,7,8,9,10]
    
    #T = 1
    #L = 16
    #J = 100
    
    low, high = get_low_high(L)
    
    #print low, high
    
    small = int(low, 2)
    large = int(high, 2)
    
    
    primes, primes_npy = small_sieve_primes(1000000000) # int(high, 10))
    # 1000000000 = ~ 22 sec. 

    jamcoins = search_jamcoins(J*3, small, large, bases)
    #print jamcoins
    print_n_jamcoins(J,jamcoins, bases)

    

def search_jamcoins(J,small,large,bases):
    global c
    jamcoins = []
    num_valid = 0
    for i in xrange(small+2, large, 2):
        c += 1
        #print("starting %d" %i)
        #found_prime = False
    
        #for base in bases:
        #    if int(bin(i)[2:] ,base) in primes:
        #        #print bin(i)[2:]+" is not valid"
        #        #print "in base: "+str(base)+" = "+str(int(bin(i)[2:], base))
        i_in_bases = set([int(bin(i)[2:], base) for base in bases])
        if len(primes.intersection(i_in_bases)) > 0:
            continue
        else:    
            jamcoins.append(bin(i)[2:])
            num_valid += 1
            if num_valid == J:
                return jamcoins                    

def print_n_jamcoins(N, jamcoins,bases):
    global c
    num_printed = 0
    for jamcoin in jamcoins:
        c += 1
        factors = [ntd(n) for n in [int(jamcoin,base) for base in bases]]
        if factors.count(None) != 0:
            continue
        else:
            print jamcoin +" "+ " ".join(map(str, factors))
            num_printed += 1
        if num_printed == N:
            break


if __name__ == "__main__":
    f = sys.stdin
    if len(sys.argv) >= 2:
        fn = sys.argv[1]
        if fn != '-':
            f = open(fn)

    T = int(f.readline())
    L, J = map(int, f.readline().split())
    
    main(T,L,J)
    #main(1, 32, 500)    
    #main(T, L, J)
    #jamcoins = search_jamcoins(J*2)
    #print_n_jamcoins(J, jamcoins)
    
    