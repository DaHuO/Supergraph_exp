fp=open('A-large.in','r')
f=0
c=0
for x in fp:
    if f==0:
        f=1
    else:
        st=''
        for y in x:
            if f==1:
                st=st+y
                f=2
            elif st[0] <= y:
                st=y+st
            elif st[0] > y:
                st=st+y
        f=1
        c=c+1
        print 'Case #%d: %s'%(c,st)
        
               
