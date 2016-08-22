def main(s):
    li=[]
    li.append(s[0])
    t=0
    for j in range(1,len(s)):
        for m in range(0,pow(2,j-1)):
            x=li[t]+s[j]
            y=s[j]+li[t]
            t+=1
            li.extend([x,y])
            
            
    t=[]
    for m in li:
        if(len(m)==len(s)):
            t.append(m)
    
    
    for n in range(0,len(s)):
        x=ord(t[0][n])
        pos=0
        for j in range(1,len(t)):
            if(x<ord(t[j][n])):
                x=ord(t[j][n])
                pos=j
        r=[]
        for i in t:
            if(ord(i[n])==ord(t[pos][n])):
                r.append(i)
        t=r[:]

    print r[0]


fo = open("A-small-attempt0.in", "r")

d2=fo.readlines()
for i in range(0,len(d2)):
    d2[i]=d2[i].rstrip()


t=int(d2[0])
for j in range(1,t+1):
    li=[]
    x=d2[j]
    print 'Case #'+str(j)+': ',
    main(x)


    
        
    
    


    
