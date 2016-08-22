from math import sqrt

def generate(N, curr='1'):
    if N == 2:
        yield curr + '1'
    else:
        for x in generate(N-1, curr + '0'):
            yield x
        for x in generate(N-1, curr + '1'):
            yield x


SMALL = None


def convert(s, base):
    ans = 0
    for p, x in enumerate(s[::-1]):
        if x == '1':
            ans += base ** p
    return ans


def isPrime(n):
    if n < 4:
        return -1
    elif n % 2 == 0:
        return 2
    upper = int(sqrt(n)) + 2
    for div in xrange(3, upper, 2):
        if n % div == 0:
            return div
    return -1

    
def solve(N, J):
    i = 0
    ans = {}
    for _ in xrange(J):
        while True:
            s = SMALL[i]
            divs = []
            for base in xrange(2, 11):
                p = isPrime(convert(s, base))
                if p == -1:
                    break
                divs.append(p)
            i += 1
            if p != -1:
                ans[s] = divs
                break
    return ans


def showSolutions(pairs):
    return '\n'.join(map(showPair, pairs.items()))


def showPair(pair):
    num, divs = pair
    return '%s %s' % (num, ' '.join(map(str, divs)))


for qq in xrange(1, int(raw_input()) + 1):
    print 'Case #%d:' % qq
    N, J = map(int, raw_input().split())
    SMALL = list(generate(N))
    ans = solve(N, J)
    print showSolutions(ans)
