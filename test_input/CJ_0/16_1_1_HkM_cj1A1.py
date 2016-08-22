def cj1A1(s):
    m=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W','X','Y','Z'];
    t=[];
    t.append(s[0]);
    for i in range(1,len(s)):
        if m.index(s[i])>=m.index(t[0]):
            t.insert(0,s[i]);
        else:
            t.append(s[i]);
    return ''.join(t);
n=input();
I=[];
for k in range(n):
    I.append(list(raw_input()))
k=1;
while k<=n:
    print 'Case #'+str(k)+': '+str(cj1A1(I[k-1]));
    k+=1;
