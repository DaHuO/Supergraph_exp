#!/usr/bin/env python

import math
import shlex

cached_primes = {}

def read_input():
    input = []
    total = -1
    with open('./input.txt') as f:
        input = f.readlines()
        total = int(input.pop(0))

    return (total, input)

def write_results(data):
    write_out = open('./output.txt', 'w')
    counter = 0

    write_out.write('Case #1:')
    write_out.write('\n')
    for value in data:
        write_out.write(str(value))
        write_out.write('\n')

    write_out.close()


PRIMES = {}
def load_primes():
    primes = []
    with open('./primes.txt') as f:
        primes = f.readlines()

    for item in primes:
        value = int(item)
        PRIMES[value] = True

def calculate_next_prime(starting_number):
    number = starting_number
    sqrt_num = math.sqrt(number)

    print 'calculating primes'

    is_prime = True
    primes = PRIMES.keys()
    primes.sort()
    while True:
        number += 2
        for prime_number in primes:
            if number % prime_number == 0:
                is_prime = False
                break
            if prime_number > sqrt_num:
                break
        if is_prime:
            PRIMES[number] = True
            return number
        else:
            is_prime = True

def is_prime_in_other_bases(candidate):
    bases = [2, 3, 4, 5, 6, 7, 8, 9]
    binary_form = bin(candidate)[2:]
    for base in bases:
        value = int(binary_form, base)
        if value in PRIMES:
            return True
    return False

def calculate_factors(n):
	fact = [1,n]
	check = 2
	rootn = math.sqrt(n)
	while check < rootn:
		if n % check == 0:
			fact.append(check)
			fact.append(n/check)
		check += 1
	if rootn == check:
		fact.append(check)
        fact.sort()
	return fact

def divisors(candidate):
    bases = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    binary_form = bin(candidate)[2:]
    result = []
    for base in bases:
        value = int(binary_form, base)
        factors = calculate_factors(value)
        print factors
        if len(factors) == 2:
            return []
        result.append(factors[1])
    return result

def prefix_check(candidate, coin_length):
    mask = 32769  # '1000000000000001'
    return ((candidate & mask) == mask)

def solve_it(coin_length, expected_count):
    size = 0
    candidate = (2**coin_length) - 1
    largest_prime = 65537
    result = []
    while size < expected_count:
        # ensure we have enough prime numbers to check against
        while candidate > largest_prime:
            largest_prime = calculate_next_prime(largest_prime)

        valid_candidate = prefix_check(candidate, coin_length)
        if valid_candidate:
            is_prime = is_prime_in_other_bases(candidate)
            if not is_prime:
                factors = divisors(candidate)
                if len(factors) > 0:
                    result.append((candidate, factors))
                    print 'found %d' % size
                    size += 1

        # loop back
        candidate -= 2

    return result


def determine_solutions(total_cases, input):
    result = []
    for i in range(0, total_cases):
        parameters = shlex.split(input[i])
        coin_length = int(parameters[0])
        number_requested = parameters[1]

        answer = solve_it(coin_length, int(number_requested))

        for candidate in answer:
            coin = bin(candidate[0])[2:].zfill(coin_length)
            validators = map(str, candidate[1])

            result.append(coin + ' ' + ' '.join(validators))

    return result

def main():
    load_primes()
    test_data = read_input()
    total_cases = test_data[0]
    input_data = test_data[1]

    results = determine_solutions(total_cases, input_data)

    write_results(results)

main()
