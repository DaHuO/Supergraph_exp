def flip(s):
    s = s[::-1]
    return ''.join('+' if c == '-' else '-' for c in s )


def solve(s):
    n = 0
    while s:
        while s[-1] == '+':
            s = s[:-1]
            if len(s) == 0:
                return n
        if s == '-'*len(s):
            return n+1
        i = 0
        while s[i] == '+':
            i += 1
        if i:
            s = flip(s[:i]) + s[i:]
            n += 1
        s = flip(s)
        n += 1
    return -23


T = int(raw_input())
i = 1
while i <= T:
    s = raw_input()
    print 'Case #{0}: {1}'.format(i, solve(s))
    i += 1

