T = int(raw_input())
for t0 in xrange(T):
    S = raw_input()
    arr = [S[0]]
    for i in xrange(len(S)):
        if i == 0:
            continue
        if ord(S[i]) >= ord(arr[0]):
            arr.insert(0, S[i])
        else:
            arr.append(S[i])
    print "Case #"+str(t0+1)+":", ''.join(arr)