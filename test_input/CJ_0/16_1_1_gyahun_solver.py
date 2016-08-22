from collections import namedtuple
from functools import reduce

Test = namedtuple('Test', 'S')

def read(line):
    return Test(line.strip())

def solve(test):
    word = reduce(lambda s, c: s + c if s[0] > c else c + s, test.S)
    return word

if __name__ == '__main__':
    infile = 'A-large.in'

    with open(infile) as src:
        lines = list(src.readlines())
    number = int(lines[0])
    tests = [read(line) for line in lines[1:]]

    with open(infile.replace('.in', '.out'), 'w') as dst:
        for i, test in enumerate(tests, 1):
            dst.write('Case #{}: {}\n'.format(i, solve(test)))
