f = open('B-large.in','r')
g = open('B-large.out','w')

a = int(f.readline())
for x in range(a):
    b = list(f.readline())[:-1]
    c = 0
    for i,y in enumerate(b):
        if i<len(b)-1 and b[i]!=b[i+1]:
            c+=1
    if b[-1]=='-':
        c+=1
    pr = 'Case #'+str(x+1)+': ' + str(c)
    print pr
    g.writelines(pr)
    g.writelines('\n')

f.close()
g.close()
