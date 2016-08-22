def solve(S):
    r = ""
    r += S[0]
    for x in S[1:]:
        if x >= r[0]:
            r = x + r
        else:
            r += x
    return r

T = int(raw_input())
for t in range(1, T+1):
    S = raw_input().rstrip();
    r = solve(S)
    print("Case #%d: %s" % (t, r))
