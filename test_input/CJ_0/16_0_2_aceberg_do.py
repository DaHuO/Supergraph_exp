'''run in same directory as input file'''
import sys
from os.path import splitext

infile_name = sys.argv[1]
infile = open(infile_name)
outfile = open('solve_{}.txt'.format(splitext(infile_name)[0]), 'w')
count = int(infile.readline())

HAPPY_SIDE, BLANK_SIDE = '+-'


def write_solution(case_nr, solution):
    outfile.write('Case #{}: {}\n'.format(i, solution))


for i, case in enumerate(range(count), 1):
    stack = infile.readline().strip()
    n_flips = 0

    for pancake in reversed(stack):
        if not n_flips % 2:
            if pancake == HAPPY_SIDE:
                continue
            elif pancake == BLANK_SIDE:
                n_flips += 1
            else:
                raise ValueError(pancake)
        else:
            # the situation is reversed
            if pancake == HAPPY_SIDE:
                n_flips += 1
            elif pancake == BLANK_SIDE:
                continue
            else:
                raise ValueError(pancake)

    write_solution(i, n_flips)
