#!/usr/bin/env python

################################################################################
#
# Google Code Jam 2016 - Qualification round
#
# Problem C - Coin Jam
#
# Victoria Lopez Morales - elkasoapy@gmail.com
#
################################################################################

import sys
import os
from random import random


def read_problem_file(filename):
    problem_list = []

    # Read the file with the input data
    out_file = open(filename, 'r')
    all_file = out_file.readlines()
    out_file.close()

    n_problems = int(all_file.pop(0).strip())

    for current_line in all_file:
        problem_list.append([int(n) for n in current_line.strip().split(' ')])

    if n_problems != len(problem_list):
        print 'Wrong formatted file!'
        sys.exit()

    return problem_list


def primes_sieve(limit):
    multiples = []
    prime_list = []

    for i in range(2, limit+1):
        if i not in multiples:
            prime_list.append(i)

            for j in range(i*i, limit+1, i):
                multiples.append(j)

    # Return the prime list
    return prime_list


def get_jamcoins(length, n_coins, max_base, prime_list):
    coins = []

    while len(coins) < n_coins:
        new_coin = '1' + ''.join(['1' if random() < 0.5 else '0' for x in range(length-2)]) + '1'

        output_coin = new_coin
        valid_coin = False

        for base in range(2,max_base+1):
            valid_coin = False
            current_base_number = int(new_coin,base)

            if current_base_number in prime_list:
                break
            else:
                for prime in prime_list:
                    if current_base_number % prime == 0:
                        output_coin += ' ' + str(prime)
                        valid_coin = True
                        break

                if not valid_coin:
                    break

        if (valid_coin):
            coins.append(output_coin)

    return coins


if __name__ == '__main__':
    # Obtain and check the given parameters
    if len(sys.argv) != 3:
        print 'Incorrect number of parameters given to this script.'
        print 'This script should be called with TWO parameters: python coin_jam.py <input_file> <output_file>'
        sys.exit()

    problems_file = sys.argv[1]
    if not os.path.isfile(problems_file):
        print 'Incorrect first parameter given to this script: ' + sys.argv[1]
        print 'The given file does not exist'
        sys.exit()

    # Read the input data
    problems_values = read_problem_file(problems_file)

    # Precompute results
    max_base = 10
    prime_list = primes_sieve(5000)

    # Process the problems
    output = []
    for index, problem in enumerate(problems_values):
        solution = get_jamcoins(problem[0], problem[1], max_base, prime_list)
        output.append('Case #' + str(index + 1) + ':')
        for coin in solution:
            output.append(str(coin))

    # Output to file
    output_file = open(sys.argv[2], 'w')
    output_file.write('\n'.join(output))
    output_file.close()
