
test=input()
w=test
m=[]
while test:
	st=raw_input()
	st=list(st)
	
	temp=""
	for a in st:
		if temp == "":
			temp=a
		elif temp[0] > a :
			temp+=a
		else:
			temp=a+temp
			
	m.append(temp)
	test=test-1
	

i=1	
for u in m:
	print "Case #"+str(i)+": "+u 
	i+=1
