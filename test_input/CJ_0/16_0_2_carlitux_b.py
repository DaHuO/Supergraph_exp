import sys

f = open(sys.argv[1])
o = open('b.txt', 'w')

tests = int(f.readline())

for step in range(1, tests + 1):
    n = [0 if x is '-' else 1 for x in f.readline()]
    s = n[::-1]
    counter = 0
    try:
        index = s.index(0)
    except:
        o.write('Case #%s: %s\n' % (step, counter))
        continue

    while index != -1:
        counter += 1
        n[0:-index] = [not x for x in n[0:-index]]
        s = n[::-1]
        try:
            index = s.index(0)
        except:
            o.write('Case #%s: %s\n' % (step, counter))
            break

o.flush()
o.close()
f.close()
