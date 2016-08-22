input=open("input.txt","r")
output=open("output.txt","w")
T = int(input.readline())
for cases in range(1,T+1):
    stack=[]
    count=0
    line = input.readline()
    [stack.append(sign) for sign in line.rstrip()]
    stack.reverse()
    while len(stack)>0 and stack[0]=='+':
        stack.remove('+')
    stack.reverse()
    print stack
    if '-' not in stack: count=0
    elif '+' not in stack: count=1
    else:
        stack.reverse()
        last_plus_index = stack.index('+')
        stack.reverse()
        last_plus_index=len(stack)-last_plus_index-1
        first_minus_index = stack.index('-')
        if first_minus_index>last_plus_index:count=2
        else:
            count=1
            for i in range(1,len(stack)):
                if stack[i-1] != stack[i]:count+=1

    output.write("Case #"+str(cases)+": "+str(count)+"\n")

input.close()
output.flush()
output.close()