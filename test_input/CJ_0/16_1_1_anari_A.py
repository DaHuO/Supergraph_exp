tcou = int(raw_input())
for tnum in range(tcou):
    s = raw_input().strip()
    t = ""
    for c in s:
        t = max(t+c, c+t)
    print "Case #{}: {}".format(tnum+1, t)

