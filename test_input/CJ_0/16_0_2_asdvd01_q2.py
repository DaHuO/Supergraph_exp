fin=open('input.in','r')
fout=open('output.txt','w')
t=int(fin.readline())
for ti in range(t):
    s=str(fin.readline())
    ans=0
    for i in range(0,len(s)):
        if i == 0 and s[i]== '-':
            ans=1
        else:
            if s[i-1]=='+' and s[i]== '-':
                ans=ans+2
    fout.write('Case #'+str(ti+1)+': '+str(ans)+'\n')
fin.close()
fout.close()
