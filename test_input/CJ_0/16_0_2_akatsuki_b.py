def magic():
    t = int(raw_input())
    for tc in xrange(t):
        s = list(raw_input())
        slen = len(s)
        res = 0
        while True:
            i = 0
            if s[i] == '-':
                while i < slen and s[i] == '-':
                    i += 1
                if i == slen:
                    res += 1
                    break
                else:
                    for j in xrange(i+1):
                        s[j] = '+'
                    res += 1
            else:
                while i < slen and s[i] == '+':
                    i += 1
                if i == slen:
                    break
                else:
                    for j in xrange(i+1):
                        s[j] = '-'
                    res += 1
        print 'Case #%d: %d' % (tc+1, res)
magic()