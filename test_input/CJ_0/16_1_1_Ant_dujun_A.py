import os
import sys

if __name__ == '__main__':
    with open('A-large.in') as w:
        T = w.readline()
        T = int(T.strip())
        for i in xrange(T):
            s = w.readline().strip()
            res = ''
            for l in s:
                if len(res):
                    if l >= res[0]:
                        res = l + res
                    else:
                        res = res + l
                else:
                    res += l
            print 'Case #%s: %s' % (i+1, res)


