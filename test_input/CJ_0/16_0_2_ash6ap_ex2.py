def yum (p):
    prev = 0;
    norm = "";
    for c in p:
        if (c != prev):
            norm = norm + c
            prev = c
    if (norm[-1] == '+'):
        norm = norm[:-1]
    return len(norm)


f = open('B-large.in', 'r')
g = open('B-large.out', 'w')
num = int(f.readline())

for i in range(1, num):
    g.write('Case #'+str(i)+': ')
    g.write(str(yum(f.readline()[:-1])))
    g.write('\n')
g.write('Case #'+str(num)+': ')
g.write(str(yum(f.readline()[:-1])))

f.close()
g.close()
