def replacee(s,l,m):
    cop_l=l
    p=''
    zp=''
    if(l==0):
        while(s[l]=='+'):
            zp=zp+'-'
            l=l+1
        return zp
    while(l>=0):
        if(s[l]=='-'):
            p=p+'+'
        if(s[l]=='+'):
            p=p+'-'
        l=l-1
    #s=s.replace(s[:cop_l+1],p)
    #print('p',p)
    return p

#s='----'
#r=replacee(s,3,0)

t=int(input())
for i in range(t):
    op=0
    s=input()
    for p in range(len(s)-1,-1,-1):
        if(s[p] == '-' and s[0]=='+'):
            z=replacee(s,0,0)
            if len(z)==1:
                s=s[:0]+z+s[1:]
            else:
                s=s.replace(s[:len(z)],z,1)
            op = op + 1
        if(s[p] == '-' and s[0]=='-'):
            z=replacee(s,p,0)
            s=s.replace(s[:p+1],z,1)
            op = op + 1
        #if(s[p] == '+'):
            #nothing
    print('case #',i+1,':',' ',op,sep="")




