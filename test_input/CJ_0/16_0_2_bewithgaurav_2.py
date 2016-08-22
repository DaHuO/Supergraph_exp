t=input()
f=1
for _ in range(t):
    a=raw_input()
    c=1
    ch=a[0]
    for i in range(1,len(a)):
        if a[i]!=ch:
            c+=1
            ch=a[i]
    if a[len(a)-1]=='+':
        c-=1
    print "Case #"+str(f)+": "+str(c)
    f+=1
