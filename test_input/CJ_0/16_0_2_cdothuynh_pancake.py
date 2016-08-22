T = int(raw_input())

for i in xrange(T):
    S = raw_input()
    z = len(S) - 1
    while S[z] == '+' and z >= 0:
        z -= 1
    S = S[:z+1]
    if len(S) == 0:
        print "Case #" + str(i+1) + ": " + str(0)
        continue
    groups = 1
    for s in xrange(len(S) - 1):
        if S[s] != S[s+1]:
            groups += 1
    print "Case #" + str(i+1) + ": " + str(groups)
    continue

