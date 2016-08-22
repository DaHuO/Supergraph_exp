def invert(size):
    if(size!=0):
        l=size-1
        for i in range(0,int(l/2)+1):
            temp=x[i]
            x[i]=x[l-i]
            x[l-i]=temp
        for i in range(0,l+1):
            if(x[i]=='+'):
                x[i]='-'
            else:
                x[i]='+'
        return 1
    return 0

def check():
    for i in x:
        if (i=='-'):
            return 1
    return 0
for j in range(int(raw_input())):
    x=list(raw_input())
    leng=len(x)
    count=0
    while(check()):
        for i in range(leng-1,-1,-1):
            if(x[i]=='-'):
                pos=i
                break
        for i in range(0,pos+1):
            if(x[i]=='-'):
                count+=invert(i)


                break
        invert(pos+1)

        count+=1

    print "Case #%d: %d" %(j+1,count)
