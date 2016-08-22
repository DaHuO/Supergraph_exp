##f = open('test.in')
##f = open('B-small-attempt0.in')
f = open('B-large.in')
f2 = open('file.txt', 'w')
f.readline()
i = 0
for l in f:
    l = l.strip()
    i += 1
    x = 0
    for j in range(len(l)-1):
        if(l[j] != l[j + 1]):
            x += 1
    if((l[0] == '-' and x % 2 == 0) or (l[0] == '+' and x % 2 != 0)):
        x += 1
    print("Case #" + str(i) + ": " + str(x),file=f2)
f.close()
f2.close()
