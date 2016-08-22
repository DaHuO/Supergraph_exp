import itertools
import sys


def evaluate(line):
    transitions = [c for c, _ in itertools.groupby(line)]
    if transitions[-1] == '+':
        return len(transitions) - 1
    else:
        return len(transitions)


if __name__ == '__main__':
    _ = sys.stdin.readline()  # skip count of test cases
    for i, line in enumerate(sys.stdin.readlines()):
        result = evaluate(line.strip())
        print 'CASE #{0}: {1}'.format(i + 1, result)
