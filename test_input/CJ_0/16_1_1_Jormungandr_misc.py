#!/usr/bin/env python

__author__ = 'Bill'


def input_(a):
    """(input_):
        function to parse code jam input
        :param a: the input file string
    """

    with open(a, 'r') as input:
        num_cases = input.readline()
        cases = input.readlines()


    return num_cases, cases


def output_(a, b):
    """(output_):
        function to write output file
        :param a: list of output cases
        :param b: name of output file
    """

    i = 1
    with open(b, 'w') as output:
        for item in a:
            output.write('Case #{}: '.format(i) + str(item) + '\n')
            i +=1
