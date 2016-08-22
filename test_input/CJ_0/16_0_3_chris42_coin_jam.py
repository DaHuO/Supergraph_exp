#!/usr/bin/env python3
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

"""
Solution to Codejam 2016 C - Coin Jam

Description:
    find numbers that consist of only 1s and 0s; the first and last number is a 1
    the number cannot be a prime number when interpreted in any base 2-10

Output:
    Case #1:
    CJ_Number b2_div .. b10_div
        bn_div - a divisor other than 1 or the number in the base, 2 - 10

Input:
    not dynamic; setting three sets
    all input is in form n j; n is the length of the codejam number
    j is the number of coinjams needed

NOTES:
    The description from Google states that you may need to do some computation beforehand
    I chose to pre-build a list of prime numbers;  I found that it takes about 7 minutes
    to generate a list of primes such that the highest one is at least 510,000
    the script will create the list and quit if the list doens't exist; then it needs to be 
    run a second time.

    The large data set takes < 5 seconds to run with the list of primes build

    I assumed that I could find the required number of coinjams with a primeness check
    that assumes a number is prime if it doesn't have a divisor below 510,000.
    Even with throwing away these false positives, all data sets can find the number of coinjams needed

"""

import sys

# I couldn't get a solution that works in any ammount of time
# Google suggests doing some processing in advanced. I will generate
# The needed prime numbers: 2 - int('1'*32) ** 0.5
# It took 20 seconds to generate the first 10,000 primes; takes 0.045 seconds to open the list of created primes
class PrimeTool(object):
    def __init__(self):
        self.primes = [2, 3, 5]
        self.last_checked = 5

    def is_prime(self, n):
        """Return True if the number is prime; otherwise return a multiple"""
        if n in self.primes:
            return True

        for p in self.primes:
            if n % p == 0:
                return p

        while self.primes[-1] < n ** 0.5:
            self.add_prime()
            new_p = self.primes[-1]
            if n % new_p == 0:
                return new_p

        return True

    def add_prime(self):
        """Add the next prime number."""
        if self.last_checked % 6 == 5:
            self.last_checked += 2
        elif self.last_checked % 6 == 1:
            self.last_checked += 4
        else:
            print("Mod 6 isn't working.")
            exit()
        n = self.last_checked
        if self.is_prime(n) == True:
            self.primes.append(n)
        else:
            return
        
def get_primes():
    """Retrieve the list of prime numbers up to the square root of the limit of int('1' * 32) ** 0.5 = 3333333333333333"""
    try:
        p_file = open("PRIMES.TXT", "r")
        primes = [int(x) for x in p_file.read().split(' ') if x != '']
        p_file.close()
    except:
        # LIMIT= 104730 # This tests the first 10,000 prime numbers
        #LIMIT= 3333333333333333
        # The above limit isn't going to complete any time soon
        # I will see if I can find an adaquate number of coinjams with
        # a list of prime numbers going up to 510,000
        LIMIT = 510000
        p_tool = PrimeTool()
        while p_tool.primes[-1] < LIMIT:
            p_tool.add_prime()
        primes = [str(x) for x in p_tool.primes]
        out_file = open('PRIMES.TXT', 'w')
        out_file.write(' '.join(primes))
        out_file.close()
        exit()
    return primes

class CJGen(object):
    """Generates potential coinjams."""
    def __init__(self, cj_len):
        self.mid_len = cj_len - 2
        self.current = 0

    def next(self):
        bits = bin(self.current).replace('0b', '')
        if len(bits) > self.mid_len:
            print("Out of numbers.")
            return None
        padding = '0' * (self.mid_len - len(bits))
        self.current += 1
        return '1' + padding + bits + '1'

class CachedPrimeTool(object):
    """Tests primeness, using a watered down attempt to speed things up."""
    def __init__(self, primes):
        self.primes = primes

    def is_prime(self, n):
        """Return True if suspected to be prime, return a multiple if one can be found in the 
            list of primes; return 0 if the number is not prime but the number doesn't have a divisor
            in the primes list
        """
        # See if divisible by any of the known primes
        for p in self.primes:
            if n % p == 0 and n != p:
                return p

        # check if the number is not prime
        mod6 = n % 6
        if not mod6 in [1, 5]:
            return 0

        return True

if __name__ == "__main__":
    primes = get_primes()
    if len(sys.argv) == 1:
        # cj_len, cj_count = 8, 32
        cj_len, cj_count = 6, 32
    elif sys.argv[1] == 's':
        cj_len, cj_count = 16, 50
    elif sys.argv[1] == 'l':
        cj_len, cj_count = 32, 500
    else:
        print("Invalid usage.")
        exit()

    prime_tool = CachedPrimeTool(primes)
    gen = CJGen(cj_len)
    found = 0
    maybe = 0
    no = 0
    out_file = sys.stdout

    out_file.write("Case #1:\n")

    while found != cj_count:
        cj = gen.next()
        multiples = []

        if cj == None:
            print("Found: {} cjs\nFound: {} maybes.\nFound: {} no".format(found, maybe, no))
            exit()

        for i in range(2, 11):
            is_prime = prime_tool.is_prime(int(cj, i))
            if is_prime == True:
                no += 1
                break
            elif is_prime == 0:
                maybe += 1
                break
            else:
                multiples.append(str(is_prime))

        if is_prime == 0 or is_prime == True:
            continue
        else:
            out_file.write("{} {}\n".format(cj, ' '.join(multiples)))
            found += 1
