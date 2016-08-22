import itertools
import math


def gen_primes(smaller_than):
    primes = [2]
    yield 2
    counter = 2

    while primes[-1] < smaller_than:
        counter += 1
        sq = int(math.sqrt(counter))
        is_prime = True
        for p in itertools.takewhile(lambda x: x<sq, primes):
            if counter % p == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(counter)
            yield counter
