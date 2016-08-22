import itertools
import math

def jamcoin_from_set(possible_jamcoin_set):
    possible_jamcoin = ''

    for digit in possible_jamcoin_set:
        possible_jamcoin = possible_jamcoin + str(digit)

    return '1' + possible_jamcoin + '1'

def get_nontrivial_divider(number):
    if number % 2 == 0:
        return str(2)

    for divider in xrange(3, int(math.sqrt(number)) + 1, 2):
        if number % divider == 0:
            return str(divider)

    return None

def get_all_nontrivial_dividers(representation_in_all_bases):
    list_of_nontrivial_dividers = []

    for number_in_base in representation_in_all_bases:
        current_nontrivial_divider = get_nontrivial_divider(number_in_base)

        list_of_nontrivial_dividers.append(current_nontrivial_divider)

        # Return as soon as one interpretation is prime
        if not current_nontrivial_divider:
            return list_of_nontrivial_dividers

    return list_of_nontrivial_dividers

number_of_lines = int(raw_input())

for line in range(1, number_of_lines + 1):
    print 'Case #{}:'.format(line)
    N, J = raw_input().split()
    N, J = int(N), int(J)

    found_jamcoins = 0

    for possible_jamcoin_set in itertools.product(range(2), repeat = N - 2):
        possible_jamcoin = jamcoin_from_set(possible_jamcoin_set)

        representation_in_all_bases = [int(possible_jamcoin, base) for base in range(2, 10 + 1)]
        non_trivial_dividers = get_all_nontrivial_dividers(representation_in_all_bases)

        if all(non_trivial_divider for non_trivial_divider in non_trivial_dividers):
            print '{} {}'.format(possible_jamcoin, ' '.join(non_trivial_dividers))

            found_jamcoins = found_jamcoins + 1

            if found_jamcoins == J:
                break;
