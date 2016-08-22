def analysis():
    t = raw_input()
    res = ""
    for i in t:
        res = max(i + res, res + i)
    return res

cases = int(raw_input())

for i in xrange(cases):
    output = "Case #%i: %s" % (i+1, analysis())
    print output
