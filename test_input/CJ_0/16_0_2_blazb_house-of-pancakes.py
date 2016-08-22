import sys
import os


def problem_specific_parser(src):
    return next(src)


def solve(data):
    flips = 0

    for e in reversed(data):
        if e == '-' and not flips & 1:
            flips += 1
        elif e == '+' and flips & 1:
            flips += 1

    return flips


def parse(src):
    lines = iter(src.split(os.linesep))
    nproblems = int(next(lines))

    for problem in range(nproblems):
        yield problem_specific_parser(lines)


def main():
    src = sys.stdin.read()
    for i, data in enumerate(parse(src)):
        print("Case #{0}: {1}".format(i + 1, solve(data)))

    
if __name__ == '__main__':
    main()
