T= int (raw_input())
counter=1

while(counter<=T):
    flip=0
    N= raw_input()
    N= list(reversed(N))
    while(N):
        stack="".join(N)
        stack=stack.lstrip('+')
        N=list(stack)
        #flipping maneuver
        for i in range(len(N)):
            if N[i]=='-':
                N[i]='+'
            else:
                N[i]='-'
        flip=flip+1
    print "Case #{}: {}".format(counter,flip-1)
    counter=counter+1
