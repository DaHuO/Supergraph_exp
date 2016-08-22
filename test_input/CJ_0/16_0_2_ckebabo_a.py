def solve(N):
    if N==0: return "INSOMNIA"
    
    n = N
    l = [0]*10
    while True:
        for c in str(n):
            l[ord(c)-ord('0')] = 1
        if sum(l) == 10:
            break
        n += N

    return n

for c in xrange(int(raw_input())):
    print "Case #%d:"%(c+1), solve(int(raw_input()))

