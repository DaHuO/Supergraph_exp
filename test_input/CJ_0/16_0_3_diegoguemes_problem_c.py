import random
import math

def non_trivial_divisor(number):
    for i in range(2, number):
        if number % i == 0:
            return i
    return None

def is_prime(number):
    if number <= 3:
        return True
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def random_jamcoin_candidate(length):
    middle = ''.join([str(random.randint(0, 1)) for _ in range(length - 2)])
    return '1' + middle + '1'

def base_interpretations(candidate):
    return [int(candidate, base) for base in range(2, 10 + 1)]

def non_trivial_divisors_for(candidate):
    return [non_trivial_divisor(base_interpretation) for base_interpretation in base_interpretations(candidate)]

def is_valid_jamcoin(candidate):
    for base_interpretation in base_interpretations(candidate):
        if is_prime(base_interpretation):
            return False
    return True

def is_valid_for_base_2(candidate):
    return candidate[-1] == '1' and not is_prime(int(candidate, 2))

def candidates(length):
    start = int('1' + '0' * (length - 2) + '1', 2)
    end = int('1' + '1' * (length - 2) + '1', 2)
    candidates = [bin(candidate)[2:] for candidate in range(start, end + 1) if is_valid_for_base_2(bin(candidate)[2:])]
    return candidates

def create_jamcoins(length, number_of_jamcoins):
    jamcoins = {}
    generated = 0
    for candidate in candidates(length):
        if is_valid_jamcoin(candidate):
            jamcoins[candidate] = non_trivial_divisors_for(candidate)
            generated += 1
        if generated == number_of_jamcoins:
            break
    return jamcoins

T = int(input())
for t in range(1, T + 1):
    length, number_of_jamcoins = [int(x) for x in input().split()]
    divisors_by_jamcoin = create_jamcoins(length, number_of_jamcoins)
    print('Case #{}:'.format(t))
    for jamcoin, divisors in divisors_by_jamcoin.items():
        print('{} {}'.format(jamcoin, ' '.join([str(x) for x in divisors])))