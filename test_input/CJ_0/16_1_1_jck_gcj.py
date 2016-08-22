import fileinput
from pathlib import Path

from tqdm import tqdm

def main(solve, pre=None, strip=True):
    cases = fileinput.input()
    n = int(next(cases))
    op = open(Path(fileinput.filename()).with_suffix('.out').name, mode='w')

    if strip:
        cases = (c.strip() for c in cases)

    if pre is not None:
        cases = (pre(c) for c in cases)

    for i, c in tqdm(enumerate(cases, 1), total=n):
        print('Case #{}: {}'.format(i, solve(c)), file=op)
