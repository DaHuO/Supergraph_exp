def solve():
    inp = list(raw_input())
    answer = ''
    for ch in inp:
        be = ch + answer
        af = answer + ch
        if be >= af:
            answer = be
        else:
            answer = af
    return answer

tc = int(input())
TC = int(tc)
while tc > 0:
    tc -= 1
    ans = solve()
    print 'Case #{}: {}'.format(TC - tc, ans)