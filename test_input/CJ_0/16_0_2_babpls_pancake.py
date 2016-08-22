fin = open('pancake.in', 'r')
fout = open('pancake.out', 'w')

count = 0

for line in fin:
    if count != 0:
        out = 0
        cur = '+'
        for x in line[:-1][::-1]:
            if cur != x:
                cur = x
                out += 1
        fout.write('Case #%d: %s\n' % (count, str(out)))
    count += 1
