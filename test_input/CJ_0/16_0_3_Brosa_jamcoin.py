from math import sqrt
from itertools import count, islice
import concurrent.futures

prime_memo = set()
def is_prime(n):
    if n in prime_memo:
        return True
    p = n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))
    if p:
        prime_memo.add(n)
    return p

def generate_jamcoin(size):
    ''' Generate `size` length Jamcoin.

    Guarantees first and last bit is 1 and only other
    characters are 0 and 1.
    '''
    assert size > 2
    for d in range(2 ** (size - 2)):
        yield '1' + bin(d)[2:].zfill(size - 2) + '1'

def jamcoin_has_prime(jamcoin):
    has_prime = False
    for base in range(2, 11):
        if is_prime(int(jamcoin, base)):
            has_prime = True
            break
    return jamcoin, not has_prime

def generate_jamcoin_proof(jamcoin):
    divisors = []

    for base in range(2, 11):
        val = int(jamcoin, base)
        for k in range(2, (val + 1) // 2):
            if val % k == 0:
                divisors.append(k)
                break
    assert len(divisors) == 9
    return jamcoin, divisors

if __name__ == '__main__':
    t = int(input())

    for i in range(t):
        n, j = tuple(map(int, input().split(' ')))
        print('Case #%d:' % (i + 1))

        with concurrent.futures.ProcessPoolExecutor() as executor:
            valid_jamcoins = []

            for jamcoin, valid in executor.map(jamcoin_has_prime, generate_jamcoin(n)):
                if valid:
                    valid_jamcoins.append(jamcoin)

                if len(valid_jamcoins) == j:
                    break

            assert len(valid_jamcoins) == j

            for jamcoin, proof in executor.map(generate_jamcoin_proof, valid_jamcoins):
                print(jamcoin, end=' ')
                print(*proof)
