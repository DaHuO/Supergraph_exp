fi = open("B-large.in", "r")
fo = open("f.out","w")
t = int(fi.readline())
for j in range(t):
	n = fi.readline()
	count = 0
	flag = False
	#count2 = 0
	for i in range(len(n)-1,0,-1):
		#print(i)
		if(flag):
			if(n[i]!=n[i-1]):
				count+=1
				count2 = 2
		else:
			if(n[i]=='-'):
				if(n[i-1]=='+'):
					count=1
				#count = 1
				flag = True
				index  = i
				#count2 += 1
				#print("hi",n[i])
	if(count==0):
		if(not ('+' in n[0:i]) ):
			st = "Case #"+str(j+1)+": 1\n"
		else:
			st = "Case #"+str(j+1)+": 0\n"
	else:
		st = "Case #"+str(j+1)+": "+str(count+1)+"\n"
	fo.write(st)
fi.close()
fo.close()
