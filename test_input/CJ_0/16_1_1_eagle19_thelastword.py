t=int(input())
k=1
while(k<=t):
    s=input()
    p=''
    for i in range(len(s)):
        if i==0:
            p=s[i]   
        elif s[i] < p[0]:
            p+=s[i]
        else:
            p=s[i]+p 
    print("Case #%s:"%k,p)
    k+=1
