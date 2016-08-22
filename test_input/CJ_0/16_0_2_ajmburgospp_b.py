t = int(raw_input())
for kei in xrange(1,t+1):
    s = raw_input()
    s = [1 if '+' == i else 0 for i in s]
    sol = 0
    for i in xrange(len(s)-1, -1, -1):
        if not s[i]:
            pos = -1
            for j in xrange(i, -1, -1):
                if s[j]:
                    pos = j
                    break
            if pos < 0:
                sol += 1
                break
            else:
                p1 = s[:pos+1]
                p2 = s[pos+1:i+1]
                p2.reverse()
                for i in xrange(len(p2)):
                    p2[i] ^= 1
                p3 = s[i+1:]
                s = p1+p2+p3
                sol += 2
    print "Case #{}: {}".format(kei, sol)