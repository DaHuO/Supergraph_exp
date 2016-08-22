def isprime(n):
    """Returns True if n is prime."""
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True

import math

def divisorGenerator(n):
    large_divisors = []
    for i in xrange(1, int(math.sqrt(n) + 1)):
        if n % i == 0 and i != 1 and i != n:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor

def get_proof(jamcoin):
    proof = []
    for base in range(2, 11):
        representation = int(jamcoin, base)
        divisors = divisorGenerator(representation)
        proof.append(str(next(divisors)))
    return proof


def verify_jamcoin(jamcoin):
    for base in range(2, 11):
        representation = int(jamcoin, base)
        if isprime(representation):
            return False
    return True


def get_jamcoins(N, J):
    # get J jamcoins
    start = "0" * N
    current = pow(2, N-1)
    target = pow(2, N) - 1

    current_jamcoins = set()

    while current != target and len(current_jamcoins) < J:
        if current % 2 == 0:
            current += 1
            continue  # jamcoins cant end in 0
        jamcoin = str(bin(current))[2:]
        if verify_jamcoin(jamcoin):
            current_jamcoins.add(jamcoin)
        current += 1

    #print current_jamcoins
    return list(current_jamcoins)

def main():
    N = 16
    J = 50
    #N = 6
    #J = 3
    jamcoins = get_jamcoins(N, J)
    answer = {}
    for jamcoin in jamcoins:
        answer[jamcoin] = get_proof(jamcoin)

    print "Case #1:"
    for jamcoin, proof in answer.iteritems():
        print "%s %s" % (jamcoin, " ".join(proof))

if __name__ == '__main__':
    main()
