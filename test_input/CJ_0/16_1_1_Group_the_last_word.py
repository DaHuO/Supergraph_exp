with open('A-large.in', 'r') as f:
    T = int(f.readline())
    for t in range(T):
        S = f.readline().strip()
        ans = S[0]
        for s in S[1:]:
            if s >= ans[0]:
                ans = s + ans
            else:
                ans += s
        print('Case #%d: %s'%(t+1,ans))
