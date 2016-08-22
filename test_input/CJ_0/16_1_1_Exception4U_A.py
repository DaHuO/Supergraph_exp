def order(a):
    b=[a[0]]
    for i in range(len(a)-1):
        if a[i+1]>=b[0]:
            b.insert(0,a[i+1])
        else :
            b.append(a[i+1])
	
    c = ''	
    for i in b:
	c=c+i	

    return c
TT = int(input())
for i in range(1,TT+1):
	a=str(raw_input())
	print "Case #"+str(i)+": "+order(a)

