g=open("input.txt","r")
h=open("output.txt","w")
t=int(g.readline())
i=0
for l in g:
    line=list(l)
    #print line
    ans=0
    while True:
        f=0
        for j in range(len(line)-1,-1,-1):
            if (line[j]=='-'):
                f=1
                for k in range(j+1):
                    if (line[k]=='-'):
                        line[k]='+'
                    elif (line[k]=='+'):
                        line[k]='-'
                ans+=1
                break
        if (f==0):
            break
    h.write("Case #%d: %d\n"%((i+1),ans))
    i+=1
h.close()
g.close()
