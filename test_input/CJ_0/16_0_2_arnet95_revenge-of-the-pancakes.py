d = {'-': 1, '+': 0}

def f(s):
    if len(s) == 1:
        return d[s]
    if s.endswith('+'):
        return f(s[:-1])
    elif s.startswith('-'):
        return 1 + f("".join([{"-":"+", "+":"-"}[c] for c in s]))
    else:
        return 1 + f('-'*s.find('-')+s[s.find('-'):])

for i in xrange(1, int(raw_input())+1):
   print "Case #%d: %d" % (i, f(raw_input()))
