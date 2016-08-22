def flip(S, n):
    for i in range((n+1)//2):
        tmp = S[n-1-i]
        S[n-1-i] = not S[i]
        S[i] = not tmp

def num_upright_bottom(S):
    c = 0
    for p in reversed(S):
        if p:
            c += 1
        else:
            break
    return c

def num_down_top(S):
    c = 0
    for p in S:
        if not p:
            c += 1
        else:
            break
    return c

def num_upright_top(S):
    c = 0
    for p in S:
        if p:
            c += 1
        else:
            break
    return c

def solve(S):
    N = len(S)
    k = num_upright_bottom(S)
    n_flips = 0
    k_prev = N
    while k < N:
        n_down_top = num_down_top(S)
        if n_down_top == 0:
            n_up_top = num_upright_top(S)
            flip(S, n_up_top)
            n_flips += 1
        """top of stack should have some facing down
        """
        flip(S, N - k)
        n_flips += 1

        k_prev = k
        k = num_upright_bottom(S)
        assert k_prev < k, "extra work"
    return n_flips

if '__main__' == __name__:
    T = int(raw_input())
    for _t in range(T):
        S = [p == '+' for p in raw_input().strip()]
        print "Case #%d: %d" % (_t+1, solve(S))
