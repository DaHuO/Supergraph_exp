for T in xrange(1, int(raw_input()) + 1):
    words = list(raw_input())

    res = words[0]

    for c in words[1:]:
        if ord(c) >= ord(res[0]):
            res = c + res
        else:
            res += c

    print "Case #%d: %s" % (T, res)
