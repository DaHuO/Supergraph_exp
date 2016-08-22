
import sys
import re
import string
import math
import random

fname = sys.argv[1]

def quick_find_divisor(num):

    # check low primes
    lowPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

    for prime in lowPrimes:
        if (num % prime == 0):
            return prime

    # didn't find one
    return 0

def find_divisor(num):
    i = 2
    max = math.sqrt(num)+1
    while i < max:
        
        if num%i == 0:
            return(i)
        # next 
        i += 1

    # not found
    return(0)

with open(fname) as f:
    # T - number of test cases
    T = int(string.split(f.readline())[0])
    #print "T {}".format(T)

    # Spin thru each test case - should only be one
    for t in range(T):
        print("Case #{}:".format(t+1))

        a = string.split(f.readline())
        # N - length of jam coin
        N = int(a[0])
        # J - number of jamcoins to create
        J = int(a[1])

        # Need to test different Jamcoins?
        # - do twice, once with quick divisor check
        for slow in range(2):
            i = 0
            coins = 0
            max = (1<<(N-2))
            while i < max:
                jamcoin = "1{}1".format(format(i, 'b').zfill(N-2))
                #print "jamcoin {}".format(jamcoin)

                # print j
                bases = []
                for j in range(9):
                    # get number in base
                    bases.append(int(jamcoin, j+2))
    
                #print "bases {}".format(bases)
    
                
                # Now find a divisor that's not 1 or the number
                found = True
                if found:
                    divisors = [0, 1, 2, 3, 4, 5, 6, 7, 8]
                    for j in range(9):
                        #print "find divisor for {}".format(bases[j])
                        if slow == 0:
                            divisors[j] = quick_find_divisor(bases[j])
                        else:
                            divisors[j] = find_divisor(bases[j])
                        #print "find_divisor returned {}".format(divisors[j])
                        if divisors[j] == 0:
                            #print "no divisor for {} base {}".format(bases[j],j+2)
                            found = False
                            break
    
                 
                # If we've found a coin print and incr coins
                if found:
                    divs = re.sub(r'[,\[\]]', '', str(divisors))
                    print("{} {}".format(jamcoin, divs))
                    coins +=  1
                    if coins == J:
                        break
    
                else:
                    #print "didn't find divisors for {}".format(jamcoin)
                    pass
    
                # add one
                i += 1

            # Did we get enough coins
            if coins == J:
                break

