from string import maketrans

t = maketrans('-+', '+-')

def flip(s, r):
    s = s[0:r][::-1].translate(t) + s[r:]
    return s

def doit(t):
    s = raw_input()
    cnt = 0
    m = s.find('-')
    while m != -1:
        p = s.find('+')
        if p == -1:
            return cnt+1
        if p > m:
            s = flip(s, p)
        else:
            s = flip(s, m)
        cnt += 1
        m = s.find('-')
    return cnt

n = int(raw_input())
for i in range(0, n):
    print "Case #%d: %d" %(i+1, doit(t))
