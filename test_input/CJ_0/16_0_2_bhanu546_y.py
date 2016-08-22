#Revenge of the Pancakes

def flip(x):
    global srr
    srr=""
    for i in x:
        if i == "+": srr+="-"
        if i == "-": srr+="+"

f=open('B-large.in','r')
out=open('outputr.txt', 'w+')
c=0
u=1
lis=[]
for k in f:
    count=0
    if c==0:
        tc = int(k)
        c=c+1
        continue
    else:
        gypsy=k
        inp = gypsy
        for j in xrange(1,len(inp)+1):
            if inp[-j]=="-" and j==1:
                x = inp[:]
                flip(x)
                inp = srr
                count+=1
            if inp[-j]=="-" and j!=1:
                x = inp[:-j+1]
                flip(x)
                inp = srr+ inp[-j+1:]
                count+=1
            else:
                continue
        count=str(count)
        count=count+"\n"
        j = "Case #{}: {}".format(u, count)
        out.write(j)
        u+=1
        lis.append(count)


f.close()
out.close()

