##
#

def doit(n):
    s = raw_input()
    m = ""
    r = ""
    for i in s:
        if not m or i >= m:
            m = i
            r = i + r
        else:
            r = r + i
    print "Case #%d: %s" %(n, r)

n = int(raw_input())
for i in range(0, n):
    doit(i+1)
