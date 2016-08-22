t=int(raw_input())
for k in xrange(t):
	S=raw_input()
	array=[]
	for j in S:
		if len(array)==0:
			array.append(j)
			continue
		if j>=array[0]:
			array.append('0')
			n=len(array)
			for i in xrange(n):
				array[n-i-1]=array[n-i-2]
			array[0]=j
		else:
			array.append(j)
	case="CASE #"+str(k+1)+": "
	s=''.join(i for i in array)
	print case+s