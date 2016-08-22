import numpy as np
import sys


def flip(x, n):
    a = x.copy()
    a[:n] = ~a[:n][::-1]
    return a

def longest_trail(x):
    diff = np.logical_xor(x, np.roll(x, -1))
    if (~diff).all():
        return len(x)
    return np.where(diff)[0][0] + 1

def find_flips(x):
    a = x.copy()
    count = 0
    while not a.all():
        a = flip(a, longest_trail(a))
        count += 1
    return count

def to_bool(s):
    return np.array(
            [int(n) for n in s.strip().replace("+", "1").replace("-", "0")]).astype(bool)

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        data = f.readlines()

    N = int(data[0].strip())
    answers = []
    for i in range(N):
        answers.append(find_flips(to_bool(data[i + 1])))

    with open(sys.argv[2], 'w') as f:
        for i, a in enumerate(answers):
            f.write("Case #{0}: {1}\n".format(i + 1, a))
