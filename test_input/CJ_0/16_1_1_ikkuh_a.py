T = int(raw_input())

for i in range(T):
    S = raw_input()
    
    results = S[0]

    for j in xrange(1, len(S)):
        if S[j] >= results[0]:
            results = S[j] + results
        else:
            results = results + S[j]
    print("Case #%d: %s" % (i+1, results))
