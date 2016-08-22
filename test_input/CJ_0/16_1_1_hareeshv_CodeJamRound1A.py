for i  in range(input()):
    r = raw_input()
    res = r[0]
    print "Case #"+str(i+1)+": ",
    for s in r[1:]:
        if s >= res[0]:
            res = s+res
        else:
            res += s
    print res