flip = { '-': '+', '+': '-'}
def flipPancakes(pancakes, n, index):
    fliped = list(pancakes)
    for i in xrange(index, n):
        fliped[i] = flip[pancakes[i]]
    return ''.join(fliped)

ts = int(raw_input())
for t in xrange(1, ts + 1):
    pancakes = raw_input()
    pancakes = pancakes[::-1]

    n = len(pancakes)
    prev = 0
    res = 0
    for i in xrange(n):
        p = pancakes[i]
        if p == '+':
            if prev != 0:
                res += 1
                pancakes = flipPancakes(pancakes, n, i - prev)
                prev = 1
        else:
            prev += 1;
    else:
        if prev != 0:
            res += 1
            pancakes = flipPancakes(pancakes, n, n - prev)

    print "Case #%d: %s"% (t, res)
