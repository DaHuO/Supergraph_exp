import fileinput
for t,l in enumerate(fileinput.input()):
    l = l.strip()
    if t == 0: continue;
    currStr = [l[0]]
    for c in l[1:]:
        if (c >= currStr[0]): currStr.insert(0, c)
        else: currStr.append(c)
    print "Case #%i: %s" % (t, "".join(currStr))
