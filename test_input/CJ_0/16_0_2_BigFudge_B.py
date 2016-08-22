#!/usr/bin/env python

def read_stdin_lines():
    import fileinput
    return [line for line in fileinput.input()]

def parse_lines(lines):
    return tuple(l.strip() for l in lines[1:])

def flip_bit(b):
    return '-' if b == '+' else '+'

def flip_bits(bs):
    return ''.join(flip_bit(b) for b in bs)

def solve(inputs):
    first_solution = {}
    first_solution['+'] = 1 if inputs[0] == '-' else 0
    first_solution['-'] = 0 if inputs[0] == '-' else 1
    solutions = [first_solution]
    for idx in range(1, len(inputs)):
        current_bit = inputs[idx]
        current_solution = {}
        possible_solutions = []
        while inputs[idx] == current_bit and idx > 0:
            possible_solutions.append(solutions[idx-1][current_bit])
            idx -= 1
        current_solution[current_bit] = min(possible_solutions)
        current_solution[flip_bit(current_bit)] = current_solution[current_bit] + 1
        solutions.append(current_solution)
    return solutions[-1]['+']

def print_outputs(outputs):
    for n, output in enumerate(outputs):
        print "Case #{}: {}".format(n+1, output)

if __name__ == '__main__':
    lines = read_stdin_lines()
    inputs = parse_lines(lines)
    outputs = map(solve, inputs)
    print_outputs(outputs)
