T = int(raw_input())

for case in xrange(1, T + 1):
    s = raw_input()
    result, s = s[0], s[1:]
    while s:
        if result[0] > s[0]:
            result, s = result + s[0], s[1:]
        else:
            result, s = s[0] + result, s[1:]

    print 'Case #{}: {}'.format(case, result)
