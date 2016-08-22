def reverse(pancakes):
    x = 0
    ready = False
    if pancakes[0] == '+':
        ready = True
    for p in pancakes:
        if p == '+':
            if not ready:
                ready = True
                x += 1
        elif p == '-':
            if ready:
                ready = False
                x += 1

    if not ready:
        x += 1
    return x

t = int(raw_input())

for i in xrange(t):
    pancakes = raw_input()
    print "Case #%d:"%(i+1), reverse(pancakes)
