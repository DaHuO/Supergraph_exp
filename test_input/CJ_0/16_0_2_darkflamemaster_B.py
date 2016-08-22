def B(s):
    res=0
    flag=True
    t=len(s)-1
    while flag:
        while t>=0 and s[t]==0:
            t-=1
        if t<0:return res
        if s[0]==1:
            s[0:t+1]=s[0:t+1][::-1]
            for j in range(t+1):
                s[j]=1-s[j]
            res+=1
        else:
            h=t-1
            while h>=0 and s[h]==1:
                h-=1
            if h<0:
                return res+1
            else:
                s[0:h+1]=s[0:h+1][::-1]
                for k in range(h+1):
                    s[k]=1-s[k]
                res+=1
            

T=int(input())

for i in range(T):
    string=input()
    s=[]
    for each in string:
        if each=='+':
            s.append(0)
        else:
            s.append(1)
    print('Case #%d: %d'%(i+1,B(s)))
    
