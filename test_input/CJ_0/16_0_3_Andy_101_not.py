def sm(m):
    d=2
    while 1:
        if m%d==0:
            return d
        elif d>5000:
            return m
        else:
            d=d+1
    
trv=[0,0,0,0,0,0,0,0,0]
ntd=[]
t=input()
for i in range(1,t+1):
    print "Case #%d:"%(i)
    nlen,j = map(int,raw_input().split(' '))
       
    while j!=0:
        s=[1]
        n = nlen-2
        for i in xrange(1<<n):
            s=s+ list(bin(i)[2:].zfill(n))
            s.append(1)
            temp=[]
            for ip in range(0,len(s)):
                temp.append(int(s[ip]))
            
            for iii in range(2,11):
                pr=0
                for ji in range(0,len(temp)):
                    pr=pr+(temp[len(temp)-ji-1]*(iii**ji))
                
                if sm(pr)!=pr:
                    trv[iii-2]=1
                    ntd.append(sm(pr))
                else:
                    trv=[0,0,0,0,0,0,0,0,0]
                    ntd=[]
                    break
            
            if 0 in trv:
                j=j
                s=[1]
            else:
                j=j-1
                nn=""
                
                for ip in range(0,len(temp)):
                    nn=nn+str(temp[ip])
                print nn,
                for ikk in ntd:
                    print ikk,
                print 
                trv=[0,0,0,0,0,0,0,0,0]
                ntd=[]
                s=[1]
                if j==0:
                    break
    
            
            
        
    
    
