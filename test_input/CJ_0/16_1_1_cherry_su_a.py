def solve_slow(S, state=""):
    if len(S) == 0:
        return state
    l = solve_slow(S[1:], S[0] + state)
    r = solve_slow(S[1:], state + S[0])
    return max(l, r)

def solve(S):
    f = [""] * (len(S) + 1)
    for i, c in enumerate(S, start=1):
        f[i] = max(c + f[i-1], f[i-1] + c)
    return f[len(S)]

if '__main__' == __name__:
    T = int(raw_input())
    for _t in range(T):
        S = raw_input().strip()
        print "Case #%d: %s" % (_t+1, solve(S))
