import numpy as np
import math


def invert(c):
    if c == '-':
        return '+'
    return '-'


def reverse(s):
    l = list(s)
    l.reverse()
    l = map(invert, l)
    return ''.join(l)


def nb_flip(s):
    s = s.rstrip('+')  # right side '+' are already placed correctly
    if len(s) == 0:
        return 0

    i = s.find('-')

    if i == 0:
        return 1 + nb_flip(reverse(s))

    return 2 + nb_flip(reverse(('-' * i) + s[i:]))


class Case:
    def __init__(self):
        self.str = ''

    def solve(self):
        return str(nb_flip(self.str))



def read_case(file):
    case = Case()
    line = file.readline()
    case.str = line.strip()
    return case


def main():
    filename_in = 'B-large.in'
    filename_out = 'B-large.out'
    file_in = open(filename_in)
    file_out = open(filename_out, 'w')

    nb_case = int(file_in.readline())

    for k in range(1, nb_case + 1):
        case = read_case(file_in)
        to_write = 'Case #' + str(k) + ': ' + case.solve()
        print to_write
        file_out.write(to_write + '\n')

    file_out.close()


if __name__ == '__main__':
    main()