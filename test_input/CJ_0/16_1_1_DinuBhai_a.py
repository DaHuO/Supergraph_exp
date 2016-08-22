# cook your code here
tt = int(raw_input())
for test in range(tt):
    l=[]
    s=raw_input()
    j=[]
    length=len(s)
    for i in range(length):
        j=[]
        if(i==0):
            j.append(s[0])
            l.append(j)
            continue
        for letters in l[i-1]:
            j.append(s[i]+letters)
            j.append(letters+s[i])
        l.append(list(j))
    ansList=l[len(l)-1]
    ansList.sort()
    print "Case #"+str(test+1)+":",ansList[len(ansList)-1]
