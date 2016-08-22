def func(p):
    n=0
    s=0
    index=0
    while index < len(p) and p[index]=='-':
        index+=1
    if index>0:
        n=1
    for i in range(index,len(p)):
        if s==0 and p[i]=='-': # encounters a - after +
            s=1
        elif s==1 and p[i]=='+': # encounters a + after -
            s=0
            n=n+2
    if s==1:
        n=n+2
    return n

T = input()
for x in range(0,T):
    p = raw_input()
    print "Case #{}: {}".format(x+1,func(p))
