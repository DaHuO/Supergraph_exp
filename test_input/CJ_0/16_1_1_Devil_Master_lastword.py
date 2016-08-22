def last():
    s=list(raw_input().strip())
    for i in xrange(1,len(s)):
        if ord(s[i])>=ord(s[0]):
            s.insert(0,s.pop(i))
    return ''.join(s)

for i in range(int(raw_input().strip())):
    print "Case #%d: %s" %(i+1,last())
