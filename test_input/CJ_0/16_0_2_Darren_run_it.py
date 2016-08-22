#!/usr/bin/env python

import collections

def read_input():
    input = []
    total = -1
    with open('./input.txt') as f:
        input = f.readlines()
        total = int(input.pop(0))

    return (total, input)

def write_results(data):
    write_out = open('./output.txt', 'w')
    counter = 0

    for index, value in enumerate(data):
        line = str(value)
        write_out.write('Case #')
        write_out.write(str(index+1))
        write_out.write(': ')
        write_out.write(line)
        write_out.write('\n')

    write_out.close()

def flip_it(pancakes, number):
    temp = []
    for i in range(0, number):
        temp.append(pancakes.popleft())

    for i in range(number-1, -1, -1):
        current = temp.pop()
        if current == '+':
            current = '-'
        else:
            current = '+'
        pancakes.appendleft(current)

def flip_front(pancakes):
    height = len(pancakes)
    found = False
    for i in range(0, height):
        if pancakes[i] == '+':
            found = True
        else:
            if i > 0 and found is True:
                return i
            else:
                return -1
    return -1

def solve_it(pancakes):
    counter = 0
    height = len(pancakes)

    for i in range(height-1, -1, -1):
        if pancakes[i] == '-':
            # We need to flip. Check front for +
            front_count = flip_front(pancakes)
            if front_count >= 0:
                flip_it(pancakes, front_count)
                counter += 1

            flip_it(pancakes, i)
            counter += 1
    return counter


def determine_solutions(total_cases, input):
    result = []
    for i in range(0, total_cases):
        pancakes = collections.deque(input[i])
        x = solve_it(pancakes)
        result.append(x)

    return result

def main():
    test_data = read_input()
    total_cases = test_data[0]
    input_data = test_data[1]

    results = determine_solutions(total_cases, input_data)

    write_results(results)

main()
