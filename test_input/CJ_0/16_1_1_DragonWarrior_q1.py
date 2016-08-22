n = input()

count = 0
for i in range(n):
    count = count + 1
    wrd = raw_input()
    l = list(wrd)
    p = []
    for j in l:
        if(len(p) == 0):
            p.append(j)
        elif(j >= p[0]):
            p.insert(0,j)
        else:
            p.append(j)
    str1 = ''.join(p)
    print "Case #"+str(count)+": "+str1
