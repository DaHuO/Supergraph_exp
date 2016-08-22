
def reverse(x, i):
    x[:i+1] = x[:i+1][::-1]
    for i in xrange(i+1):
        x[i] = '-' if x[i] == '+' else '+'


def brute(start):
    l = len(start)
    last = list('+' * l)
    mi = 10 ** 9

    Q = [(start, 0)]
    S = {tuple(start): 0}
    while Q:
        x, moves = Q.pop()
        if x == last:
            mi = min(mi, moves)
            continue
        for i in xrange(l):
            tmp = [z for z in x]
            reverse(tmp, i)
            if tuple(tmp) not in S or S[tuple(tmp)] > moves+1:
                Q.append((tmp, moves+1))
                S[tuple(tmp)] = moves+1
    return mi


def solve(t):
    start = list(raw_input())
    l = len(start)
    last = list('+' * l)
    ans = 0

    while last != start:
        for i in xrange(l-1, -1, -1):
            if last[i] != start[i]:
                reverse(last, i)
                ans += 1
                break
    print 'CASE #%d: %d' % (t, ans)

T = input()
for i in xrange(T):
    solve(i+1)
