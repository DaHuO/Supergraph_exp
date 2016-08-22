n = int(raw_input())
for itt in xrange(n):
    seq = raw_input().strip() + '+'
    # solving the probem
    last_sym = seq[0]
    cnt = 0
    for sym in seq[1:]:
        if sym != last_sym:
            last_sym = sym
            cnt += 1
    print 'Case #' + str(itt + 1) + ': ' + str(cnt)
