t=int(input())
for i in range(t):
    s=input()
    a=s[0]
    for j in range(1,len(s)):
        if(ord(a[0])>ord(s[j])):
            a="".join(a)+s[j]
        else:
            a=s[j]+"".join(a)
    print("Case #{0}: {1}".format(i+1,a))        
