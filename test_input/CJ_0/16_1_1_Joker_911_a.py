with open('A-small.in','r') as f:
	t=int(f.readline())
	for i in range(t):
		st=f.readline().rstrip()
		ch1=''
		ch2=''

		for j in range(len(st)):
			ch1+=st[j]
			ch2=st[j]+ch2
			if ch2>ch1:
				ch1=ch2
			elif ch1>ch2:
				ch2=ch1
		print("Case #"+str(i+1)+": "+ch1)

