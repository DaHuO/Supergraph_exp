t = int(raw_input())
for i in range(1,t+1):
    S = raw_input()
    count = 0
    for j in range(1,len(S)):
        if(S[j]!=S[j-1]):
            count +=1
    if(S[-1]=='-'):
        count +=1
    print ("Case #"+str(i)+": "+str(count))
    
