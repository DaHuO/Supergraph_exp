t=input()
for tc in range(t):
	s=raw_input()
	a=[]
	for el in s:
		a.append(ord(el)-ord('A'))
	curr=[]
	curr.append(a[0])
	a.remove(a[0])
	l=len(s)
	while len(curr)!=l:
		if curr[0]<=a[0]:
			curr.insert(0,a[0])
		else:
			curr.append(a[0])
#		print curr
		a.remove(a[0])
	for i in range(len(curr)):
		curr[i]=chr(curr[i]+ord('A'))
	print "Case #"+str(tc+1)+":",''.join(curr)