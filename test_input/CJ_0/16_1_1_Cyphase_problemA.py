from __future__ import print_function

import sys

try:
    input = raw_input
except NameError:
    pass


def main():
    num_cases = input()

    for case_idx, s in enumerate(iter(sys.stdin.readline, ''), 1):
        lastword = s[0]
        for c in s[1:].strip():
            if c >= lastword[0]:
                lastword = c + lastword
            else:
                lastword += c

        print("Case #{}: {}".format(case_idx, lastword))


if __name__ == '__main__':
    main()
