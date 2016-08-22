import math
import sys
import time


#start =
#{
#    16: 32769,      # 2^(16-1)+1 --> 1000000000000001
#    32: 2147483649  # 2^(32-1)+1
#}


def baseN(num,b,numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
    return ((num == 0) and numerals[0]) or (baseN(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])


def from_binary(number, base):
    array = [int(i) for i in number]
    array.reverse()
    num = 0
    i = 0
    for digit in array:
        num += math.pow(base, i) * digit
        i+=1
    return int(num)


def is_prime(n):
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


def find_nontrivial_factor(x):
   for i in range(2, 20):
       if x % i == 0:
           return i


def find_jamcoins(N, J):
    start = int(math.pow(2, N-1) + 1)
    for j in xrange(0,J):
        while True:
            b = baseN(start,2)
            if not b.startswith("1"):
                start += 2
                continue
            non_primes = []
            for base in xrange(2,11):
                val = from_binary(b,base)
                if not is_prime(val):
                    non_primes.append(val)
            if len(non_primes) != 9:
                start += 2
                continue
            non_trivial_factors = []
            for val in non_primes:
                factor = find_nontrivial_factor(val)
                if factor is None:
                    break
                non_trivial_factors.append(str(factor))
            if len(non_trivial_factors) != 9:
                start += 2
                continue
            print("{0} {1}".format(str(b), ' '.join(non_trivial_factors)))
            start += 2
            break


if __name__ == "__main__":
    T = int(raw_input())
    for i in xrange(1, T + 1):
        user_input = raw_input().split(' ')
        N = int(user_input[0])
        J = int(user_input[1])
        print("Case #{0}: ".format(i))
        find_jamcoins(N, J)
