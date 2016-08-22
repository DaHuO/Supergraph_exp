from sys import stdin as sin
t = int(sin.readline())
for i in range(1,t+1):
    n = (sin.readline().rstrip('\n'))
    c=n[0]
    for j in range(1,len(n)):
        #print (c[0])
        if c[0]<=n[j]:
            c=n[j]+c
        else:
            c=c+n[j]
    print('Case #%d: %s'%(i,c))
    
