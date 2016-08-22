#!/usr/bin/env pypy
import sys

lines = iter(sys.stdin)
next(lines)  # throw away first line


def main():
    for case, line in enumerate(lines, 1):
        print 'Case #%i:' % case
        N, J = (int(x) for x in line.split())

        answers = 0
        for coin in range(2 ** (N-2)):
            coin = '1%s1' % format(coin, '0%sb' % (N-2))
            factors = []
            for base in range(2, 11):
                i = int(coin, base)
                for factor in (2, 3, 5, 7, 11):
                    if i % factor == 0:
                        factors.append(factor)
                        break
                else:
                    break
            if len(factors) == 9:
                print coin, ' '.join(str(f) for f in factors)
                answers += 1
                if answers >= J:
                    break

if __name__ == '__main__':
    exit(main())
