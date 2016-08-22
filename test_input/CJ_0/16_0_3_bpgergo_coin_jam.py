# https://code.google.com/codejam/contest/6254486/dashboard#s=p2
import pickle
import fileinput
from functools import lru_cache


def rwh_primes(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return set([2] + [i for i in range(3,n,2) if sieve[i]])


def get_digits(n):
    result = list()
    while n:
        result.append(n % 10)
        n //= 10
    return result


def interpret_in_base(n, base):
    return sum([base ** i * d for i, d in enumerate(get_digits(n))])


def generate_num(n, length):
    return int('1' + '{0:b}'.format(n).zfill(length - 2) + '1')


@lru_cache(maxsize=None)
def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def is_jamcoin(n, primes):
    result = True
    for base in range(2, 11):
        x = interpret_in_base(n, base)
        result = result and not x in primes
    return result


def is_jamcoin(n):
    result = True
    for base in range(2, 11):
        x = interpret_in_base(n, base)
        result = result and not is_prime(x)
    return result


def find_divisor(n):
    for y in range(2, n):
        if n % y == 0:
            return y
    return None


def build_divisors(n, primes):
    result = {1: None}
    for i in range(2, n+1):
        if i in primes:
            result[i] = None
        else:
            result[i] = find_divisor(i)
    return result


def get_divisors(n, primes):
    result = list()
    for base in range(2, 11):
        x = interpret_in_base(n, base)
        result.append(primes[x])
    return result


@lru_cache(maxsize=None)
def get_divisors(n):
    result = list()
    for base in range(2, 11):
        x = interpret_in_base(n, base)
        result.append(find_divisor(x))
    return result


def main():
    f = fileinput.input()
    T = int(f.readline())
    assert (T == 1)
    print("Case #1:")
    N, J = (int(s.strip()) for s in f.readline().split())
    MAX = 10 ** N
    """
    try:
        primes = pickle.load(open("primes.pickle", "rb"))
        divisors = pickle.load(open("divisors.pickle", "rb"))
    except (OSError, IOError) as e:
        primes = rwh_primes(MAX)
        divisors = build_divisors(MAX, primes)
        pickle.dump(primes, open("primes.pickle", "wb"))
        pickle.dump(divisors, open("divisors.pickle", "wb"))
    """
    nums = (generate_num(i, N) for i in range(MAX))
    cnt = 0
    for i, num in enumerate(nums):
        if is_jamcoin(num):
            print(" ".join(map(str, [num] + get_divisors(num))))
            cnt += 1
        if cnt >= J:
            break

if __name__ == '__main__':
    main()
