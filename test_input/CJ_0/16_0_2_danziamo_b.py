test_cases = int(raw_input())

for case in xrange(1, test_cases+1):
    s = raw_input()
    p = s[0]
    f = 0
    for i in xrange(1 ,len(s)):
        if s[i] != p:
            p = s[i]
            f += 1
    if p == '-':
        f += 1
    print "Case #{}: {}".format(case, f)
