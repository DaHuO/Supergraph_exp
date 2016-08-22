import sys

t = int(sys.stdin.readline())

def getstring(s):
    wordrank = sorted(list(s))
    ret = ''
    for x in s:
        if ret == '':
            ret = x + ret
        else:
            if ret[0] <= x:
                ret = x + ret
            else:
                ret = ret + x
    return ret

for i in range(t):
    ret = ''
    s = sys.stdin.readline().strip()
    print "Case #%d:" % (i + 1),  getstring(s)
