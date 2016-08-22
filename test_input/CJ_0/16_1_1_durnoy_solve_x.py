from __future__ import print_function

import fractions
import sys

def calc(S):
    out = S[0]
    for ch in S[1:]:
        if ch >= out[0]:
            out = ch + out
        else:
            out = out + ch
    return out

def main():
    f = sys.stdin

    if len(sys.argv) > 1:
        f = open(sys.argv[1], "rt")

    T = int(f.readline().strip())

    for case_id in range(1, T+1):
        s = f.readline().strip()

        r = calc(s)

        print(str.format('Case #{}: {}', case_id, r))

if __name__ == '__main__':
    main()
