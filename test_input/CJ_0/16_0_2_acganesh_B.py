from itertools import groupby
from random import randint

def num_flips(s):
    groups = [''.join(grp) for num, grp in groupby(s)]
    n = len(groups) - 1
    n_flips = 0

    while n >= 0:
        if '-' in groups[n]:
            groups = flip(groups, n)
            n_flips += 1
        n -= 1
    return n_flips

def swap(s):
    length = len(s)
    if s[0] == '+':
        return '-'*length
    else:
        return '+'*length

def flip(groups, n):
    return map(swap, groups[:n+1]) + groups[n+1:]

def main():
    T = int(raw_input())
    for i in xrange(1, T+1):
        s = raw_input()
        print 'Case #%s: %s' % (i, num_flips(s))


def get_random(N):
    s = ''
    for _ in xrange(N):
        if randint(0, 1) == 0:
            s += '-'
        else:
            s += '+'
    return s

def test_large():
    for _ in xrange(100):
        s = get_random(100)
        print s, num_flips(s)

def validate():
    assert num_flips('-') == 1
    assert num_flips('-+') == 1
    assert num_flips('+-') == 2
    assert num_flips('+++') == 0
    assert num_flips('--+-') == 3
    print 'Tests passed!'


#test_large()
main()
