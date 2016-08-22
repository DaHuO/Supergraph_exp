t = int(raw_input())
for i in range(0,t):
    seq = raw_input()
    c = 0
    for j in range(1,len(seq)):
        if seq[j] != seq[j-1]:
            c += 1
    if seq[len(seq)-1] == '-':
        c += 1
    print 'Case #%d: %d' % (i+1,c)
