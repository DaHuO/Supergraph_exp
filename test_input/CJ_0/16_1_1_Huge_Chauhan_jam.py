T=eval(input())
for z in range(T):
    inp=input()
    array=list(inp[0])
    for i in range(1,len(inp)):
        if inp[i] >= array[0]:
            array.insert(0,inp[i])
        else:
            array.append(inp[i])
    r="".join(str(m) for m in array)
    print("Case #{}: {} ".format(z+1,r))
