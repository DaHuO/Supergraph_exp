def ch(j,x):
    if(x[j]=='+'):
        x[j]='-'
    elif(x[j]=='-'):
        x[j]='+'
    return x



def rev(x):
    x=list(x)
    l=len(x)
    count=0
    while(1):
        if(x.count('+')==l):
            return count
        count+=1
        
        if(x[0]=='+'):
            i=1
            while(i<l):
                if(x[i]=='-'):
                    break;
                i+=1
            for j in range(0,i):
                x=ch(j,x)
                
        elif(x[0]=='-'):
            i=1
            while(i<l):
                if(x[i]=='+'):
                    break;
                i+=1
            for j in range(0,i):
                x=ch(j,x)
    return count

fo = open("B-large.in", "r")

d2=fo.readlines()
for i in range(0,len(d2)):
    d2[i]=d2[i].rstrip()

t=int(d2[0])

for j in range(1,t+1):
    li=[]
    x=d2[j]
    print 'Case #'+str(j)+': ',
    c=rev(x)
    print c


