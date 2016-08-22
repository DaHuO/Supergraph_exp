def solve():
    S = raw_input()
    s = S[0]

    for i in range(1,len(S)):
        if S[i] >= s[0]:
            s = S[i]+s
        else:
            s = s + S[i]

    return s

T = input()

for t in range(1,T+1):
    print("Case #%d: %s" % (t,solve()))
