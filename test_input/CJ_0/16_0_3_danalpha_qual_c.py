#!/usr/bin/env python
# -*- coding: utf-8 -*-

magic_numbers = {
    16: [3, 2, 5, 2, 7, 2, 3, 2, 7],
    32: [3, 2, 5, 2, 7, 2, 3, 2, 11]
}


def num_for_base(bin_string, pows):
    num = 0
    for index, c in enumerate(bin_string[::-1]):
        if c == '1':
            num += pows[index]
    return num


def find_divisor(bin_string, pows, base):
    num = num_for_base(bin_string, pows)
    # print "num", num

    magic = magic_numbers[32][base-2]
    if num % magic == 0:
        return magic
    else:
        return -1

    # if num % 2 == 0:
    #     return 2
    #
    # cur = 3
    # while cur*cur <= num:
    #     if num % cur == 0:
    #         return cur
    #     cur += 2
    #
    # return -1


def solve(cipher):
    parts = cipher.split()
    n = int(parts[0])
    j = int(parts[1])

    pows_for_base = {base:[base**i for i in xrange(0, n)] for base in xrange(2, 11)}
    # print pows_for_base

    result = "\n"

    min_val = 2**(n-1) + 1
    max_val = 2**n - 1

    current = min_val
    found = 0

    while found < j:
        divisors = []
        bin_string = format(current, 'b')
        # print "bin_string", bin_string

        for base in xrange(2, 11):
            d = find_divisor(bin_string, pows_for_base[base], base)
            if d == -1:
                break
            else:
                divisors.append(str(d))

        if len(divisors) == 9:
            result_str = "{} {}\n".format(bin_string, ' '.join(divisors))
            # print "FOUND: ", result_str
            result += result_str
            found += 1
        # else:
        #     print "naw", current

        current += 2
        if current > max_val:
            raise Exception()

    return result

if __name__ == "__main__":
    testcases = input()

    for case_num in xrange(1, testcases+1):
        cipher = raw_input()
        print("Case #%i: %s" % (case_num, solve(cipher)))
