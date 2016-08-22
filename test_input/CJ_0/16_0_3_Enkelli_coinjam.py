#!/usr/bin/env python3

from math import sqrt
import sys


def get_file_content(f):
    with open(f, 'r') as input_file:
        return input_file.read()


def get_divisor(num, base):
    num = int(str(bin(num)[2:]), base)
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return i
    return None


def coinjam(length, count):
    num = int('1' + '0' * (length - 2) + '1', 2)
    for i in range(count):
        found = False
        while not found:
            found = True
            divisors = []
            for j in range(2, 11):
                n = get_divisor(num, j)
                if not n:
                    found = False
                    break
                else:
                    divisors.append(str(n))
            num += 2
        print(bin(num - 2)[2:] + " " + ' '.join(divisors))


def main(argc, argv):
    if argc < 2:
        print("Hey man, give me some file.")
        sys.exit(1)

    jam = get_file_content(argv[1]).split()
    print("Case #1:")
    coinjam(int(jam[1]), int(jam[2]))
    


if __name__ == '__main__':
    sys.exit(main(len(sys.argv), sys.argv))
