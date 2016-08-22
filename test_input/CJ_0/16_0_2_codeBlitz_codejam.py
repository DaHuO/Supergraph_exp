T = int(raw_input())
counter=0
f = open("codejamop.txt","w")
for i in range(0,T):
	counter=0
	string = list(raw_input())
	j=0
	if string[len(string)-1]=='-':
			counter+=1
	for j in range(len(string)-1):
		if j== len(string)-1:
			break
		else:
			if string[j]!=string[j+1]:
				counter+=1

	f.write("Case #%d: %d\n" % (i+1,counter))		

	
