n = int(raw_input().strip())
for case in xrange(1, n + 1):
    pancakes = raw_input().strip()[::-1]
    flip = 0
    result = 0
    for i in xrange(len(pancakes)):
        if (pancakes[i] == '+') ^ flip == 0:
            flip = 1 - flip
            result += 1
    print 'Case #%d: %d' % (case, result)
