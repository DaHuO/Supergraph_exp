t=int(input())
for i in range(t):
    s=input()
    if(s[len(s)-1]=='+'):
        temp=0
    else:
    	temp=1
    for j in range(len(s)-1):
    	if(s[j]!=s[j+1]):
    		temp+=1
    	
    print('Case #{0}: {1}'.format(i+1,temp))
        
