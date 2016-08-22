import numpy as np
INPUT_TXT = 'input.txt'
OUTPUT_TXT = 'output.txt'
OUTPUT_TEMPLATE = 'Case #{}: {}\n'
R = 'r'
W = 'w'


def solve(input_line):
    pancakes = input_line[::-1]
    number_of_flips = 0
    plus = "+"
    minus = "-"
    for pancake in pancakes:
        if pancake == minus:
            number_of_flips += 1
            minus, plus = plus, minus
    return number_of_flips


def main():
    with open(INPUT_TXT, R) as input_file, open(OUTPUT_TXT, W) as output_file:
        for i, input_line in enumerate(input_file):
            if not i:
                continue
            output_line = solve(input_line.replace('\n', ''))
            output_file.write(OUTPUT_TEMPLATE.format(i, output_line))


if __name__ == "__main__":
    main()
