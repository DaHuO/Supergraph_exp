t=int(raw_input().strip())
for _ in xrange(t):
    print 'Case #{}:'.replace('{}',str(_+1)),
    x=raw_input()
    trunc=len(x)
    while trunc>0 and x[trunc-1]!='-':
        trunc-=1
    x=x[:trunc]
    #print x,
    if len(x)==0:
        print 0
        continue
    count=1
    prev=x[0]
    for i in xrange(1,len(x)):
        if x[i]!=prev:
            count+=1
        prev=x[i]
    print count
    
    
