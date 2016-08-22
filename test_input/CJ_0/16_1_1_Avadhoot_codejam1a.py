T=int(raw_input())
for i in range(T):
    S=list(raw_input())
    last=list()
    last.append(S[0])
    for j in S[1:]:
        if j<last[0]:
            last.append(j)
        elif j>=last[0]:
            last.insert(0,j)
    print "Case #1: "+"".join(last)
