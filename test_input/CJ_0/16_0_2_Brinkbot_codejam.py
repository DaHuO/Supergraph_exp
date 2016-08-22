import sys
import numpy as np


def parse_and_solve(inp):
    line = next(inp)
    return str(np.diff(np.fromiter((c == '-' for c in line), bool, len(line))).sum())


def main():
    num = int(next(sys.stdin))
    for i in range(1, num + 1):
        sys.stdout.write('Case #{:d}: {}\n'.format(
            i, parse_and_solve(sys.stdin)))


if __name__ == '__main__':
    main()
