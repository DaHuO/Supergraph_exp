#!/usr/bin/env python

################################################################################
#
# Google Code Jam 2016 - Round 1A
#
# Problem A - The Last Word
#
# Victoria Lopez Morales - elkasoapy@gmail.com
#
################################################################################

import sys
import os


def read_problem_file(filename):
    problem_list = []

    # Read the file with the input data
    out_file = open(filename, 'r')
    all_file = out_file.readlines()
    out_file.close()

    n_problems = int(all_file.pop(0).strip())

    for current_line in all_file:
        problem_list.append(current_line.strip())

    if n_problems != len(problem_list):
        print 'Wrong formatted file!'
        sys.exit()

    return problem_list


def last_word(input_letters):
    output_letters = input_letters[0]

    for letter in input_letters[1:]:
        if letter >= output_letters[0]:
            output_letters = letter + output_letters
        else:
            output_letters = output_letters + letter

    return output_letters


if __name__ == '__main__':
    # Obtain and check the given parameters
    if len(sys.argv) != 3:
        print 'Incorrect number of parameters given to this script.'
        print 'This script should be called with TWO parameters: python last_word.py <input_file> <output_file>'
        sys.exit()

    problems_file = sys.argv[1]
    if not os.path.isfile(problems_file):
        print 'Incorrect first parameter given to this script: ' + sys.argv[1]
        print 'The given file does not exist'
        sys.exit()

    # Read the input data
    problems_values = read_problem_file(problems_file)

    # Process the problems
    output = []
    for index, problem in enumerate(problems_values):
        solution = last_word(problem)
        line = 'Case #' + str(index + 1) + ': ' + str(solution)
        output.append(line)

    # Output to file
    output_file = open(sys.argv[2], 'w')
    output_file.write('\n'.join(output))
    output_file.close()
