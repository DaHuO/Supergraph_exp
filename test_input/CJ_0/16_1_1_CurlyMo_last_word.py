#!/usr/bin/env python
import argparse


def main(infile, out):
    for line in read_input(infile, out):
        S = list(line)
        last_word = list(S.pop(0))
        for char in S:
            if char >= last_word[0]:
                last_word.insert(0, char)
            else:
                last_word.append(char)

        out.write(''.join(last_word) + '\n')


def read_input(infile, out):
    with open(infile, 'r') as f:
        num_cases = int(f.readline())
        for case in range(1, num_cases+1):
            out.write('Case #{}: '.format(case))
            yield f.readline().rstrip()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="codejam qual A")
    parser.add_argument('input', type=str,
                        help='Input file')
    parser.add_argument('output', type=argparse.FileType('w'),
                        help='Output file')
    args = parser.parse_args()
    main(args.input, args.output)
