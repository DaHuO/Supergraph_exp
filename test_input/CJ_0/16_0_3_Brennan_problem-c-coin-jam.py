
from __future__ import division
import math
import itertools


def is_evenly_divisible(divisor, dividend):
    # Exceptional cases.
    if dividend / divisor < 1:
        return False
    if dividend % divisor == 0:
        return True
    return False


def first_non_1_factor(number):

    if number == 1:
        return None
    if number == 2:
        return 2

    # We only need to check up to the sqrt of n.
    square_root = int(math.ceil(math.sqrt(number)))
    top_of_range = square_root + 1
    # We don't need to check any even numbers besides 2.
    range_to_check = itertools.chain([2],  itertools.count(3, 2))  # This is infinite.

    for divisor in range_to_check:
        if divisor > 1000:
            break  # Give up, for speed.
        if divisor > top_of_range:  # Break when we hit the top of divisors to check.
            break

        if is_evenly_divisible(divisor, number):
            return divisor
    return None


def dec_to_bin(dec):
    return int(bin(dec)[2:])


def get_jam_coin_divisors(possible_jam_coin):
    divisors_for_bases = []
    for base in xrange(2, 11):
        int_for_base = int(possible_jam_coin, base)
        first_factor = first_non_1_factor(int_for_base)
        if first_factor:
            divisors_for_bases.append(str(first_factor))
        else:
            return []
    return divisors_for_bases

num_problems = int(raw_input())
n, required_num_solutions = [int(i) for i in raw_input().split(" ")]
num_digits_in_between = n - 2
max_value_in_between_number = int(math.pow(2, num_digits_in_between) - 1)

jam_coins_found = []
print "Case #1:"
for x in xrange(max_value_in_between_number+1):
    in_between_part = str(dec_to_bin(x)).zfill(num_digits_in_between)
    possible_jam_coin_str = "1" + in_between_part + "1"
    divisors = get_jam_coin_divisors(possible_jam_coin_str)
    if len(divisors):
        jam_coins_found.append(possible_jam_coin_str)
        print "%s %s" % (possible_jam_coin_str, " ".join(divisors))
        if len(jam_coins_found) == required_num_solutions:
            break
