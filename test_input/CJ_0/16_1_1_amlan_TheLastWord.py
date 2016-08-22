t = int(input())

for caseno in range(1,t+1):
	s = str(input())
	ls = []
	for sx in s:
		l = len(ls)
		flag=True
		for i in range(l):
#			print(i,ls[i],sx)
			if(ls[i]<sx):
				ls = [sx]+ls
				flag=False
				break
			elif(ls[i]>sx):
				ls.append(sx)
				flag=False
				break
		if(flag):
			ls.append(sx)
	s = ''.join(ls)
	print("Case #%d: %s"%(caseno,s))
