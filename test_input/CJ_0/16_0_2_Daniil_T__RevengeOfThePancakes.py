for test in range(input()):
    print "Case #%d:" % (test+1),

    count = 0
    last = '+'

    for cookie in reversed(raw_input()):
        if cookie != last:
            count += 1
            last = cookie

    print count
