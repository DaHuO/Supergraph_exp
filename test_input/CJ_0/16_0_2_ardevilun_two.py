import sys
T=int(sys.stdin.readline())
for a in range(1,T+1):
	st = list(sys.stdin.readline())[:-1]
	count=0
	st1 = list(reversed(st))
	while(st1[count] != '-'):
		count+=1
		if count == len(st):
			break
	st = st[0:len(st)-count]

	count = -1
	while True:
		if len(st)==1:
			if st[0] == '-':
				count +=1
				break
		elif len(st)==0:
			break
		else:
			count+=1
			for i in range(0,len(st)-1):
				if st[i] != st[i+1]:
					count +=1
					
			break
	print("Case #"+str(a)+": "+str(count+1))