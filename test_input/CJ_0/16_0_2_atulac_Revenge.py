inp=open('B-large.in')
out=open('output.txt','w')
for test_case in range(int(inp.readline().strip())):
    s=inp.readline().strip()
    l=len(s)
    if s[l-1]=='-':
        ans=1
        check1='+'
        check2='-'
    else:
        ans=0
        check1='-'
        check2='+'
    for i in range(l-2,-1,-1):
        if s[i]==check1:
            ans+=1
            check1,check2=check2,check1

    out.write("Case #"+str(test_case+1)+": "+str(ans)+"\n")
inp.close()
out.close()
            
            
    
            
            
