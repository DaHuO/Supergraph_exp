import sys
import random

def readline():
    return sys.stdin.readline().rstrip()

was = set()

def randcoin(n):
    while True:
        s = '1'
        for _ in range(n-2):
            s += random.choice('01')
        s += '1'

        if s in was:
            continue
        was.add(s)

        return s

def divisors(s):
    ans = []
    for k in range(2, 11):
        x = long(s, k)

        ok = False
        for d in xrange(2, 10000):
            if x%d == 0:
                ans.append(d)
                ok = True
                break
        if not ok:
            return None
    return ans

def solve():
    readline()
    n, j = map(int, readline().split())

    print 'Case #1:'
    while j > 0:
        s = randcoin(n)

        d = divisors(s)
        if not d:
            continue

        print s, ' '.join(map(str, d))

        j -= 1


if __name__ == '__main__':
    solve()

