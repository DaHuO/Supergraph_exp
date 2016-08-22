tc=int(raw_input())
for i in range(tc):
    a=raw_input()
    n=len(a)
    #a=list(a)
    s=a[0]
    for j in range(1,n):
        if a[j]>=s[0]:
            s=a[j]+""+s[0::]
        else:
            s=s[0::]+""+a[j]
    print "Case #"+(str)(i+1)+": "+s
