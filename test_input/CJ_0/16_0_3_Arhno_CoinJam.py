import numpy as np
import math
import time


def find_div(n):
    start = time.time()
    if n % 2 == 0:
        return 2

    stop = math.sqrt(n)
    k = 3
    while k < stop:
        if time.time() - start > 0.03:
            return 0
        if n % k == 0:
            return k
        k += 2

    return 0


class Case:
    def __init__(self):
        self.N = 0
        self.J = 0

    def solve(self):
        res = '\n'
        j = 0
        cj = (1 << (self.N - 1)) + 1
        while j < self.J:
            diviseurs = []
            s = "{0:b}".format(cj)
            print 'processing', s
            for k in range(2, 11):
                n = int(s, k)
                div = find_div(n)
                if div > 0:
                    diviseurs.append(div)
                else:
                    break

            if len(diviseurs) == 9:
                res += s + ' ' + ' '.join(map(str, diviseurs)) + '\n'
                j += 1

            cj += 2

        return res


def read_case(file):
    case = Case()
    line = file.readline().split(' ')
    line = map(int, line)
    case.N = line[0]
    case.J = line[1]
    return case


def main():
    filename_in = 'C-large.in'
    filename_out = 'C-large.out'
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