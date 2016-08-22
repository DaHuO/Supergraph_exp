from sys import stdin, stdout
import pyprimes

PRIMES = pyprimes.erat(2 ** 22)

def getDivisor(n):
    """ adapted from 'isprime_division' method of pyprimes library """
    if n < 2:
        return -1
    limit = n**0.5
    for divisor in PRIMES:
        if divisor > limit: break
        if n % divisor == 0: return divisor
    return -1


def solve(N, J):
    current = int("1" + "0"*(N-2) + "1", 2)

    solutions = []
    while len(solutions) < J:
        current_bin = "{0:b}".format(current)
        if current_bin[0] == "1" and current_bin[-1] == "1":
            divisors = []
            for base in range(2, 11):
                divisor = getDivisor(int(current_bin, base))
                if divisor == -1:
                    break
                else:
                    divisors.append(divisor)

            if len(divisors) == 9:
                soln = "{0:b}".format(current)
                for divisor in divisors:
                    soln += " %s"%divisor

                solutions.append(soln) 

        current += 1

    return "\n" + "\n".join(solutions)


T = int(stdin.readline())

for t in range(T):
    N, J = map(int, stdin.readline().strip().split())

    result = solve(N, J)

    stdout.write("Case #%d: %s\n"%(t+1, result))