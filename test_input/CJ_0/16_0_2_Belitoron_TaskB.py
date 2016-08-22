import itertools

fi = open('D:\B-large.in', 'r')
fo = open('D:\output.txt', 'w')

z = int(fi.readline())
for i in range(1, z+1):
    s = ''.join(ch for ch, _ in itertools.groupby(fi.readline().strip()))
    if s.endswith('+'):
        s = s[:-1]
    fo.write('Case #{0}: {1}\n'.format(i, len(s)))
