from math import sqrt

# Returns the jamcoin string of the decimal number n.
def to_jamcoin(n):
    return "{:b}".format(n)

# Returns the binary representation of the decimal number n as a list.
def to_binary(n):
    return [int(i) for i in to_jamcoin(n)]

# Converts the decimal number n to base b.
def convert(n, b):
    return sum([e * (b ** i) for i, e in enumerate(to_binary(n)[::-1])])

# Returns the smallest nontrivial divisor of the decimal number n converted to
# base b; if there is no such divisor, returns -1 instead.
def find_divisor(n, b):
    n_b = convert(n, b)

    # The following method relies on the fact that if n_b has a divisor greater
    # than sqrt(n_b), then it also has a divisor less than sqrt(n_b), so we only
    # need to search up to sqrt(n_b). We could be more efficient by noting that
    # we only need to search for prime factors, which are of the form 6k +- 1
    # (except for 2). This is because if there is a nontrivial composite
    # divisor, then a prime factor of this divisor is also a nontrivial divisor
    # of n_b.
    for i in range(2, int(sqrt(n_b)) + 1):
        if n_b % i == 0:
            return i

    return -1

# Number of test cases.
T = input()

for i in range(T):
    N, J = [int(j) for j in raw_input().split()]

    jamcoins = []

    # In decimcal, the first jamcoin is 2 ** (N - 1) + 1 and each subsequent
    # jamcoin is 2 greater than the last. We can iterate as such until we get
    # to 2 ** N, in which case we stop since the jamcoin is now of length
    # greater than N.
    for n in range(2 ** (N - 1) + 1, 2 ** N, 2):
        jamcoin = to_jamcoin(n)
        valid = True

        # Iterate through all bases from 2 to 10, inclusive, to check whether
        # the current jamcoin is valid.
        for k in range(2, 11):
            divisor = find_divisor(n, k)

            if divisor == -1:
                valid = False
                break
            else:
                jamcoin += " %d" % divisor

        # If we have found a valid jamcoin, then add it to the list of jamcoins
        # and check whether we need to find more jamcoins.
        if valid:
            jamcoins.append(jamcoin)

            if len(jamcoins) == J:
                break

    print "Case #%d:" % (i + 1)

    for line in jamcoins:
        print line