# -*- coding: utf-8 -*-


def flip(s):
    return [not e for e in reversed(s)]


def complement(s):
    return [not e for e in s]


def solve(s):
    visited = set()
    q = [(s, 0)]
    while q != []:
        s, ret = q.pop(0)
        if all(s):
            return ret

        visited.add(tuple(s))

        for i in xrange(len(s)):
            ns = flip(s[:i + 1]) + s[i + 1:]
            if tuple(ns) not in visited:
                q.append((ns, ret + 1))


def main():
    t = int(raw_input())
    for i in xrange(1, t + 1):
        s = raw_input()
        seq = [e == '+' for e in s]
        print 'Case #%d:' % i,
        print solve(seq)


if __name__ == '__main__':
    main()
