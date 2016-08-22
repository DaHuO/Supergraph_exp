import re

with open('B-large.in', 'rb') as fin, open('out.txt', 'wb') as fout:
    n = int(fin.readline().strip())
    cs = 0

    for _ in range(n):
        p = fin.readline().strip()
        c = 0
        cs += 1

        while(not re.match('^\++$', p)):
            if p.startswith('-'):
                p = re.sub('^-+', '+', p)
                c += 1
            else:
                p = re.sub('^\++', '-', p)
                c += 1
        fout.write('Case #{}: {}\n'.format(cs, c))
