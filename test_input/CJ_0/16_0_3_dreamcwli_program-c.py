#!/usr/bin/env python

from __future__ import print_function

def decompose(number):
    floor = int(number ** 0.5) + 1
    for x in range(3, floor, 2):
        if number % x == 0:
            return x
    return 1

cases = raw_input()
cases = int(cases)

for case in range(1, cases + 1):
    line = raw_input()
    length, count = [int(x) for x in line.split(' ')]

    output = 'Case #%d:' % case
    print(output)

    string = '1' + '0' * (length - 2) + '1'
    while True:
        divisors = []
        for base in range(2, 11):
            number = int(string, base)
            divisor = decompose(number)
            if divisor == 1:
                divisors = []
                break
            else:
                divisors.append(divisor)

        if divisors:
            print(string, end='')
            for divisor in divisors:
                print(' %d' % divisor, end='')
            print()

            count -= 1
            if not count:
                break

        number = int(string, 2) + 2
        string = format(number, 'b')
        if len(string) > length:
            break
