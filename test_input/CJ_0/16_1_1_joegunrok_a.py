from sys import stdin as IN
for _ in range(int(IN.readline())):
    print "CASE #%s:" % (_+1),
    w = IN.readline().strip()
    ret = ""
    for i in range(len(w)):
        if not ret or w[i] >= ret[0]:
            ret = w[i] + ret
        else:
            ret = ret + w[i]
    print ret
