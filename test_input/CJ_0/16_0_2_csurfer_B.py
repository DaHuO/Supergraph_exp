def solve():
    pancakes = raw_input()
    flips = 0
    for i in xrange(1, len(pancakes)):
        if pancakes[i] != pancakes[i-1]:
            flips += 1
    if pancakes[-1] == '-':
        flips += 1
    return flips

tc = int(input())
TC = int(tc)
while tc > 0:
    tc -= 1
    ans = solve()
    print 'Case #{}: {}'.format(TC - tc, ans)