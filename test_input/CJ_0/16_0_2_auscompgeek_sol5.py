#!/usr/bin/env pypy3


def flip(S, i):
    #return [not x if j < i else x for j, x in enumerate(S)]
    s = [not x for x in S[:i]]
    s += S[i:]
    return s


def solve(S):
    last = None

    for i, c in enumerate(S):
        if i is 0:
            last = c
            continue

        if c is not last:
            return solve(flip(S, i)) + 1

    else:
        return last


def parse(S):
    return [x == '-' for x in S]


def main():
    T = int(input())
    for x in range(1, T+1):
        print('Case #%d: %d' % (x, solve(parse(input()))))


if __name__ == "__main__":
    main()
