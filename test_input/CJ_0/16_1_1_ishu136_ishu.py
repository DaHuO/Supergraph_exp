t=int(input())
for x in range(t):
    str=input()
    l1=len(str)
    s1=""
    temp=""
    s1+=str[0]
    i=1
    while(i<l1):
        if(s1[0]>str[i]):
            s1+=str[i]
        else:
            temp+=s1
            s1=""
            s1+=str[i]
            s1+=temp
            temp=""
        i+=1
    print('case #{}: {}'.format(x+1,s1))
    
        
        
        