def flip(pattern,stack,happy):
    if pattern==list("+"):
        happy=True
        return 0,stack,happy
    elif pattern==list("-"):
        happy=True
        return 1,stack,happy
    elif pattern==list("+-"):
        i=0
        while stack[i]!='-':
            stack[i]='-'
            i+=1
        happy=True
        return 2,stack,happy
    elif pattern==list("-+"):
        happy=True
        return 1,stack,happy
    elif pattern==list("+-+"):
        i=0
        while stack[i]!='-':
            stack[i]='-'
            i+=1
        return 1,stack,happy
    elif pattern==list("-+-"):
        temp=list()
        i=0
        while stack[i]!='+':
            temp.append('+')
            i+=1
        while stack[i]!='-':
            temp.append('-')
            i+=1
        while i<len(stack) and stack[i]!='+':
            temp.append('+')
            i+=1
        for i in range(len(temp)-1,-1,-1):
            stack[len(temp)-i-1]=temp[i]
        return 1,stack,happy
        
    
T=int(raw_input())
for i in range(T):
    S=raw_input()
    stack=list(S)
    happy=False
    nflips=0
    
    while not happy:
        pattern=list(stack[0])
        for j in range(1,len(stack)):
            if stack[j]!=pattern[-1]:
                pattern.append(stack[j])
        x=0
        if len(pattern)>=3:
            x,stack,happy=flip(pattern[:3],stack,happy)
            nflips+=x
        else:
            x,stack,happy=flip(pattern[:],stack,happy)
            nflips+=x
    print "case #"+str(i+1)+": "+str(nflips)
        



'''
#1
T=int(raw_input())
for i in range(T):
    N=int(raw_input())
    digits=set()
    c=1
    n=N
    if N==0:
        print "case #"+str(i+1)+": INSOMNIA"
        continue
    while len(digits)!=10:
        for j in str(n):
            digits.add(j)
            #print digits
        n=c*N
        c+=1
    #print n,c,N
    c-=2
    n=c*N
    print "case #"+str(i+1)+": "+str(n)
'''
