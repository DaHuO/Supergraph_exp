def main():
    file = open("/home/aidan/Documents/codejam16/C-large.in")
    outFile = open("/home/aidan/Documents/codejam16/C-large.out", "w")

    file.readline() # Only one test
    line = file.readline()
    length, count = [int(x) for x in line.split()]
    tally = 0  # Amount of jamcoins found
    outFile.write("Case #1:\n")
    primes = genPrimes(10000)
    jamcoin = str(1 * 10**(length-1) + 1)
    while tally < count:
        factors = isValidJamcoin(jamcoin, primes)
        if factors:
            outFile.write("{0} {1}\n".format(
                jamcoin, " ".join((str(x) for x in factors))))
            tally += 1
        jamcoin = format(int(jamcoin,2) + 2, 'b')

'''
Returns a list of factors, or False
'''
def isValidJamcoin(coin, primes):
    bases = []
    factors = []
    for index in range(2, 11):
        bases.append(int(coin, base=index))
    for i, x in enumerate(bases):
        # Try to find a factor
        base = i + 2
        optFactor = findFactor(x, primes)
        if optFactor == -1:
            # Next jamcoin
            return False
        else:
            factors.append(optFactor)
    return factors


def findFactor(n, primes):
    for prime in primes:
        if n % prime == 0:
            return prime
    return -1


def genPrimes(n):
    count = 2
    primes = []
    while count < n:
        if isPrime(count, primes):
            primes.append(count)
        count += 1
    return primes


def isPrime(number, primes):
    for prime in primes:
        if number % prime == 0:
            return False
    return True

if __name__ == "__main__":
    main()