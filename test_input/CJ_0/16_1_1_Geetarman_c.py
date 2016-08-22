import sys

f = open(sys.argv[1])
rid = open(sys.argv[2], 'w')

tcnt = int(f.readline().strip())

for i in xrange(tcnt):
    w = f.readline().strip()
    print w

    max_ch = max(w) 

    r = w[0]
    j = 1
    while j < len(w) and w[j] != max_ch:
        if r[0] <= w[j]:
            r = w[j] + r
        else:
            r = r + w[j]
        j += 1

    if j < len(w):
        r = w[j] + r
        j += 1

    while j < len(w):
        if w[j] == max_ch:
            r = w[j] + r
        else:
            r = r + w[j]
        j += 1
        

    resultstr = 'Case #%d: %s' % (i + 1, r)
    rid.write(resultstr + '\n')
    

f.close()
rid.close()
