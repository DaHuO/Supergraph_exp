
ALL_PRIMES = []

# Sieve of Eratosthenes
# Code by David Eppstein, UC Irvine, 28 Feb 2002
# http://code.activestate.com/recipes/117119/

def buildPrimes(max):
    """ Generate an infinite sequence of prime numbers.
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}
    
    # The running integer that's checked for primeness
    q = 2
    
    while q < max:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            # 
            ALL_PRIMES.append(q)
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next 
            # multiples of its witnesses to prepare for larger
            # numbers
            # 
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        
        q += 1

def isPrime(n):
    for i in ALL_PRIMES:
        if n % i == 0:
            return i
        if i > (n // 2) + 1:
            break
    return 0

def testPrime():
    # for i in range(1, 100):
    #     o = isPrime(i)
    #     if o == 0:
    #         print("%d is prime" % (i))
    #     else:
    #         print("%d is not prime (divisible by %d)" % (i, o))
    for i in ALL_PRIMES:
        print("%d is prime" % (i))

def main():
    numInputs = int(input())
    for i in range(numInputs):
        N, J = (int(c) for c in input().split(' '))
        print("Case #%d:" % (i + 1))
        j = 0
        n = 0
        while j < J and n < 2 ** (N - 2):
            # print("n =", n)
            s = '1' + ("{0:0" + str(N - 2) + "b}").format(n) + '1'
            # print("s =", s)
            # r = [str(isPrime(int(s, k))) for k in range(2, 11)]
            r = list()
            for k in range(2, 11):
                c = str(isPrime(int(s, k)))
                # print("k, c =", k, c)
                if c != '0':
                    r.append(c)
                else:
                    break
            if len(r) == 9:
                print(s + " " + " ".join(r))
                j += 1
            # else:
            #     print(s + " x")
            n += 1

if __name__ == '__main__':
    import sys
    buildPrimes(2 ** 16)
    if '-d' in sys.argv:
        testPrime()
        pass
    else:
        main()