inp=open('A-large.in')
out=open('outputLarge.txt','w')
for test_case in range(int(inp.readline().strip())):
    word=inp.readline().strip()
    ans=''
    for each in word:
        if ans=='':
            ans+=each
        else:
            if each<ans[0]:
                ans+=each
            else:
                ans=each+ans
    out.write("Case #"+str(test_case+1)+": "+ans+"\n")

inp.close()
out.close()
                
