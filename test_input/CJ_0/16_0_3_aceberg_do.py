'''run in same directory as input file
NOTE: run with python3
'''
import sys
from os.path import splitext

infile_name = sys.argv[1]
infile = open(infile_name)
outfile = open('solve_{}.txt'.format(splitext(infile_name)[0]), 'w')
count = int(infile.readline())
assert count == 1

outfile.write('Case #1:\n')
length, target = (int(c) for c in infile.readline().split())


class NoDivisor(Exception):
    pass


def get_divisor(number, max_attempt=200):
    '''attempt to get a divisor, else raise NoDivisor'''
    # quick return on even values
    if not number % 2:
        return 2

    max_divisor = min(int(number ** .5), max_attempt)
    for divisor in range(3, max_divisor, 2):
        if not number % divisor:
            return divisor

    raise NoDivisor()


def write_solution(jamcoin, divisors):
    divisors_string = ' '.join([str(n) for n in divisors])
    outfile.write('{} {}\n'.format(jamcoin, divisors_string))


def main():
    coins_found = 0
    make_jamcoin = '1{{:0{}b}}1'.format(length - 2).format
    max_permutations = 2 ** (length - 2)

    for i in range(0, max_permutations):
        jamcoin = make_jamcoin(i)
        try:
            divisors = [get_divisor(int(jamcoin, base=base))
                        for base in range(2, 11)]
        except NoDivisor:
            continue

        write_solution(jamcoin, divisors)
        coins_found += 1
        print('found {}/{}: {}'.format(coins_found, target, jamcoin))
        if coins_found == target:
            break
    else:
        raise Exception('Could not find sufficient jamcoins!')


if __name__ == '__main__':
    main()
