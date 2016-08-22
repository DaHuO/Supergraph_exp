# Preparation: find prime numbers using modified Sieve of Eratosthenes
# I treat 2 as a special case (for performance reasons only) and so only odd numbers are used

ARR_SIZE = 32768

isPrime = [True] * ARR_SIZE
primes = []

for index in xrange(ARR_SIZE):
    if isPrime[index]:
        # 3, 5, 7, 9, 11, 13, 15,
        number = index*2+3
        primes.append(number)
        for i in xrange(index, ARR_SIZE, number):
            isPrime[i] = False


def find_divisor(num):
    # special case: number is even
    if num & 1 == 0:
        return 2

    from math import sqrt
    max_prime = sqrt(num)

    for prime in primes:
        if prime > max_prime:
            return 0
        if num % prime == 0:
            return prime

    # nothing found, number is prime
    return 0

# Real work

for test in range(input()):
    print "Case #%d:" % (test+1)

    bits, count = map(int, raw_input().split())

    # 100..001
    coinValue = (1 << (bits-1)) + 1

    while count > 0:
        coin = bin(coinValue)[2:]
        isGood = True
        divisors = []

        for radix in xrange(2, 11):
            converted = int(coin, radix)
            divisor = find_divisor(converted)
            if divisor == 0:
                isGood = False
                break
            else:
                divisors.append(divisor)

        if isGood:
            count -= 1
            print coin, " ".join("%d" % x for x in divisors)

        coinValue += 2