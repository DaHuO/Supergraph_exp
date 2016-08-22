#! /usr/bin/env python3

import sys

if (len(sys.argv) > 1):
    input_filename = sys.argv[1]
else:
    input_filename = "input.txt"


def find_rightmost(stack, symbol):
    for i in range(len(stack) - 1, -1, -1):
        if stack[i] == symbol:
            return i


def sol(stack):
    if stack.find('-') == -1:
        return 0

    stack = stack.strip()
    end = len(stack)

    symbols = ['-', '+']
    symbol_index = 0
    symbol = symbols[symbol_index]

    num_flips = 0
    while end != 0:
        end = find_rightmost(stack[0:end], symbols[symbol_index])

        if end is None:
            break

        num_flips += 1
        symbol_index = (symbol_index + 1) % 2

    return num_flips



with open(input_filename, 'r') as f:
    num_cases = int(f.readline())

    for i in range(num_cases):
        stack = f.readline()
        solution = sol(stack)
        print("Case #{}: {}".format(i+1, solution))
        

