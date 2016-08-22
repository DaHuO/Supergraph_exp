inf = open('A-large.in', 'r')
outf = open('output.txt', 'w')

t = int(inf.readline().strip())

for i in range(t):
    c = inf.readline().strip()
    s = ''
    for j in c:
        if s == '' or j >= s[0]:
            s = j + s
        else:
            s = s + j
    outf.write('Case #{}: {}\n'.format(i+1, s))
