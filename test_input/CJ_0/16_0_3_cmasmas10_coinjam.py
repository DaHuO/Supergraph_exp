import sys
import numpy
from primes import primesfrom2to


#Code for generating prime numbers
#from http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/3035188#3035188
def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = numpy.ones(n/3 + (n%6==2), dtype=numpy.bool)
    for i in xrange(1,int(n**0.5)/3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k/3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)/3::2*k] = False
    return numpy.r_[2,3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)]

def convert_to_base(binary_number,base):
    number_converted = 0
    current_base = 1
    for d in reversed(binary_number):
        number_converted+=int(d)*current_base
        current_base*=base
    return number_converted

def get_divisor(n,primes):
    max_value = math.sqrt(n)
    for prime in primes:
        if n % prime == 0:
            return prime
        if prime > max_value:
            return None

def check_coinjam(n,primes):
    divisors = []
    for base in range(2,11):
        candidate_in_base = convert_to_base(n,base=base)
        divisor = get_divisor(candidate_in_base,primes)
        if divisor is None:
            return []
        divisors.append(str(divisor))
    return divisors


if __name__ == "__main__":
    import math
    T = int(sys.stdin.readline()) #number of test cases

    for i in xrange(1,T+1):
        N,J = sys.stdin.readline().split(' ')
        N = int(N)
        J = int(J)
        print 'Case #%d:'%i

        min_value = 2**(N-1) +1    #First and last digits are 1
        max_value = 2**N - 1       #All 1's

        #Generate primes
        MAX_PRIME = 100000
        primes = primesfrom2to(MAX_PRIME)

        j = 0
        for candidate in xrange(min_value,max_value,2):
            candidate_binary = bin(candidate)[2:]
            divisors = check_coinjam(candidate_binary,primes)
            if divisors:
                print candidate_binary, ' '.join(divisors)
                j+=1
            if j == J: #we are done
                break
