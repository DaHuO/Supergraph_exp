t=input()
count=1
while count<=t:
    inp=raw_input().strip()
    res=inp[0]
    for i in range(1,len(inp)):
        if ord(res[0])>ord(inp[i]):
            res=res+inp[i]
        else:
            res=inp[i]+res
    print "Case #"+str(count)+": "+res
    count+=1
