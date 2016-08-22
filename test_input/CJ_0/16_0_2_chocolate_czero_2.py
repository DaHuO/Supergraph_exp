outF = open("B-large.out","w")

with open("B-large.in","r") as inF:
    t= int(inF.readline())
    for it in xrange(t):
        s = inF.readline().strip()
        n = 2 * s.count('+-')
        if s[0] == '-':
        	n += 1
        print "Case #%d: %d"%((it+1), n)
        outF.write("Case #%d: %d\n"%((it+1), n))

outF.close()

print "done"