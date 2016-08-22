import sys

for cases in xrange(int(sys.stdin.readline())):
    s = sys.stdin.readline().strip()
    if s.count('-') == 0:
        c = 0
    elif s.count('+') == 0:
        c = 1
    elif len(s) == 1:
        c = 1
    else:
        c = 0
        pos = len(s)
        for i in s[::-1]:
            if i == '-':    break
            pos -= 1
        s1 = ''
        if s[0] == '-':
            c = 1
            for i in s[:pos]:
                if i == '+':    s1 = '-' + s1
                else:   s1 = '+' + s1
            #print "s1 = ",s1

            if pos != len(s):
                s = s1 + s[pos:]
            #print "s = ",s

            pos = len(s)
            for i in s[::-1]:
                if i == '-':    break
                pos -= 1
        
        if pos == len(s):   pos -= 1
        prev = s[0]
        for i in xrange(1,pos+1):
            if prev == '+' and s[i] == '-':
                c += 2
            prev = s[i]
    print "Case #%d: %d"%(cases+1,c)
