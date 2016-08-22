def check(l):
    if l[0] == '+' and len(list(set(l))) == 1:
        return True
    return False

def invert_index(S, f_elm):
    for z in xrange(len(S)):
        if f_elm == '-' and S[z] == '+':
            return z
        elif f_elm == '+' and S[z] == '-':
            return z

def invert(l, a, b):
    ex = l[a]
    if ex == '-':
        l[a:b] = '+'
    else:
        l[a:b] = '-'
    return l

t = int(raw_input())
for x in xrange(t):
    S = raw_input()
    l = list(S)
    ans = 0
    for y in xrange(len(S)):
        if check(l):
            break
        inv_index = invert_index(l, l[0])
        l = invert(l, 0, inv_index)
        ans += 1
    print "Case #%i:"%(x+1), ans
        
                
