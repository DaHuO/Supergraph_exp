T = input()

for i in xrange(1, T+1):
    s = raw_input()
    ln = len(s)
    cnt = 0
    j = 0
    prev = ''
    while j < ln:
        #print s[j]
        if s[j] == '-':
            while (j < ln) and (s[j] == '-'):
                j += 1
            if prev == '+':
                cnt += 1
            prev = '-'
            cnt += 1
        else:
            while (j < ln) and (s[j] == '+'):
                j += 1
            prev = '+'

    print "case #" + str(i) + ": " + str(cnt)
