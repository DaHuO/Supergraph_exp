import sys, itertools, random, pdb


def gen_coins(N):
    for seq in itertools.product("01", repeat=N-2):
        yield "1{0}1".format("".join(seq))


def rwh_primes1(n):
    """ Returns a list of primes x in [a, b] """
    sieve = [True] * (n/2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]


def rabinMiller(num):
    # Returns True if num is a prime number.

    s = num - 1
    t = 0
    while s % 2 == 0:
        # keep halving s while it is even (and use t
        # to count how many times we halve s)
        s = s // 2
        t += 1

    for trials in range(5): # try to falsify num's primality 5 times
        a = random.randrange(2, num - 1)
        v = pow(a, s, num)
        if v != 1: # this test does not apply if v is 1.
            i = 0
            while v != (num - 1):
                if i == t - 1:
                    return False
                else:
                    i = i + 1
                    v = (v ** 2) % num
    return True


def isPrime(num):
    # Return True if num is a prime number. This function does a quicker
    # prime number check before calling rabinMiller().

    if (num < 2):
        return False # 0, 1, and negative numbers are not prime

    # About 1/3 of the time we can quickly determine if num is not prime
    # by dividing by the first few dozen prime numbers. This is quicker
    # than rabinMiller(), but unlike rabinMiller() is not guaranteed to
    # prove that a number is prime.
    global lowPrimes

    if num in lowPrimes:
        return True

    # See if any of the low prime numbers can divide num
    for prime in lowPrimes:
        if num % prime == 0:
            return False

    # If all else fails, call rabinMiller() to determine if num is a prime.
    #return rabinMiller(num)


def main():
    global lowPrimes
    lowPrimes = rwh_primes1(10 ** 6)

    f = open(sys.argv[1], 'r')
    T = int(f.readline().strip())

    for t in xrange(T):
        N, J = map(int, f.readline().strip().split(' '))
        print "Case #{0}:".format(t+1)

        num_coin = 0
        for coin in gen_coins(N):
            divisors = []
            for base in xrange(1, 10):
                val = int(coin, base+1)
                if isPrime(val):
                    break
                else:
                    for prime in lowPrimes:
                        if val % prime == 0:
                            divisors.append(prime)
                            break
            if len(divisors) == 9:
                num_coin += 1
                print "{0} {1}".format(coin, " ".join(str(d) for d in divisors))
                if num_coin == J:
                    break


if __name__ == "__main__":
    main()
