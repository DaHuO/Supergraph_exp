"""

"""

import sys


if __name__ == '__main__':

    with open(sys.argv[1], 'r') as f:

        n_test_cases = int(f.readline())
        test_cases = []

        for i in range(n_test_cases):
            test_cases.append(f.readline()[:-1])

    solutions = []
    for s in test_cases:
        candidate = [s[0]]
        for c in list(s[1:]):
            if c >= candidate[0]:
                candidate.insert(0, c)
            else:
                candidate.append(c)

        solutions.append(''.join(candidate))

    with open('lastword-large.txt', 'w') as f:
        n = 1
        s_lst = []
        for solution in solutions:
            s_lst.append("Case #%d: %s" % (n, solution))
            n += 1

        f.write('\n'.join(s_lst))
