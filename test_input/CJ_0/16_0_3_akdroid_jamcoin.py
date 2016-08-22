
N=16
s=['0']*N
s[0]='1'
s[N-1]='1'
main_list=["".join(s)]

for j in range(1,N-2):
    s1=list(s)
    s1[j]='1'
    for k in range(j+1,N-1,2):
        s2=list(s1)
        s2[k]='1'
        main_list.append("".join(s2))
case_id = 1

#mlist = set(main_list)
#print len(mlist)

print "Case #1:"
for num in main_list:
    print num,
    for i in range(3,12):
        print i,
        if(int(num,i-1)%i!=0):
            print "Error"
    print 
