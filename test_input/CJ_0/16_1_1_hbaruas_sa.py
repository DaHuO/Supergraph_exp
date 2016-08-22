times=int(input())
for x in range (times):
    inpt=input()
    inp=[]
    result=[]
    for z in inpt:
        inp.append(z)
    result.append(inpt[0])   
    for zx in range(1,len(inpt)):
        if(result[0]>inp[zx]):
            result.append(inp[zx])
        else:
            result.insert(0,inp[zx])
    asd=str(x+1)
    str1 = ''.join(result)
    print("Case #"+asd+": "+str1)
            
            
