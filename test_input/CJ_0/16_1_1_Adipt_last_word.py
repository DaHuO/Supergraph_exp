t = int(raw_input())
u = 0
while u<t:
    u+=1
    s = raw_input()
    r = ''
    for i in s:
        if i+r>r+i:
            r = i+r
        else:
            r = r+i
    print "Case #%d: %s" %(u, r)
