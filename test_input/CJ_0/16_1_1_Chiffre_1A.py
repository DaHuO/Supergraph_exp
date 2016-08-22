def last_word(s):
    final=s[0]
    for i in range(1,len(s)):
        if s[i]>=final[0]:
            final=s[i]+final
        else:
            final=final+s[i]
    return final


t=int(raw_input())
l=[]
for j in range(t):
    l.append(raw_input())

for k in range(t):
    print 'Case #'+str(k+1)+': '+last_word(l[k])
