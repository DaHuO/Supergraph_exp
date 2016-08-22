fi = open('input')
fo = open('output', 'w')

T = int(fi.readline())

for Ti in range(1, T + 1):
    l = fi.readline().strip()
    ch = 0
    t = l[0]
    for c in l:
        if c != t:
            ch += 1
            t = c
    if l[len(l) - 1] == '-':
        ch += 1

    print("Case #%d: %d" % (Ti, ch))

fi.close()
fo.close()
