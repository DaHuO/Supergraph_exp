f=open('A-small-attempt0.in.txt', 'r')
r=open('result.txt', 'w')



l=int(f.readline())
for t in range(1,1+l):
    print t
    tmp=f.readline()
    tmp=tmp[::-1]
    tmp=list(tmp)
    cnt=0
    for i in range(len(tmp)):
        if tmp[i]=='-':
            for j in range(i, len(tmp)):
                if tmp[j]=='-':
                    tmp[j]='+'
                else:
                    tmp[j]='-'
            cnt+=1

    r.write('Case #'+str(t)+': '+str(cnt)+'\n')


