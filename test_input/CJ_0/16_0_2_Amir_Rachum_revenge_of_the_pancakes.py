import os
import time
import pytest
import collections
from contextlib import contextmanager
from typing import List


INPUT_TYPE = 'large'

Case = collections.namedtuple('Case', ['pancakes'])

"""
class Pancake(object):
    def __init__(self, happy):
        self.happy = happy

    def flip(self):
        self.happy = not self.happy

    def is_happy(self):
        return self.happy


class PancakeStack(list):
    def __init__(self, pancakes):
        for i in pancakes:
            self += [Pancake(happy=(i == '+'))]

    def flip(self, index):
        self[:index] = [pancake.flip() for pancake in reversed(self[:index:])]
"""


def solve(case: Case):
    """break 'case', solve and return the solution"""
    current = case.pancakes[0]
    blank_groups = int(current == '-')

    for pancake in case.pancakes:
        if pancake == current:
            continue
        current = pancake
        if current == '-':
            blank_groups += 1

    if case.pancakes[0] == '+':
        return 2 * blank_groups
    else:
        return 2 * blank_groups - 1


def read_case(lines: List[str]) -> Case:
    """Read a test case from the input."""
    return Case(pancakes=lines.pop(0).strip())


def read_file(filepath: str) -> List[Case]:
    """Read the input `filepath` and return a list of cases."""
    cases = []
    with open(filepath, 'rt') as fobj:
        lines = fobj.readlines()
        num_cases = int(lines.pop(0))
        for _ in range(num_cases):
            cases.append(read_case(lines))
    return cases


def write_results(results: List, outfile: str) -> None:
    with open(outfile, 'wt') as f:
        for idx, result in enumerate(results):
            f.write('Case #{}: {}\n'.format(idx + 1, result))


@contextmanager
def timing(prefix):
    start = time.time()
    yield
    print('{} took {} seconds.'.format(prefix, time.time() - start))


def main(infile: str, outfile: str) -> None:
    cases = read_file(infile)
    results = []
    for idx, case in enumerate(cases):
        with timing("Solving case #{}".format(idx + 1)):
            results.append(solve(case))
    write_results(results, outfile)


test_cases = {
    Case(pancakes='-'): 1,
    Case(pancakes='-+'): 1,
    Case(pancakes='+-'): 2,
    Case(pancakes='+++'): 0,
    Case(pancakes='--+-'): 3,
}


@pytest.mark.parametrize(('case', 'result'), test_cases.items())
def test_function(case: Case, result):
    assert solve(case) == result


if __name__ == '__main__':
    if INPUT_TYPE:
        main(os.path.join('io', '{}.in'.format(INPUT_TYPE)),
             os.path.join('io', '{}.out'.format(INPUT_TYPE)))
    pytest.main(args=[__file__])
