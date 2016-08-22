t=int(input())
for j in range (t):
    l=list(input())
    a=len(l)
    i=0
    count=0

    while(i<(a-1) and i!=(a-1)):
        if(l[i]!=l[i+1]):
            count+=1
            i+=1
        else:
            i+=1
    if(l[a-1]=='-'):
        print("Case #{}: {}".format(j+1,count+1))
    else:
        print("Case #{}: {}".format(j+1,count))
            
        
    
        
            
        
            