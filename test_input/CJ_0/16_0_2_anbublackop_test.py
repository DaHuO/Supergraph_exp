for _ in range(int(input())):
	cakes=list(input())
	number=len(cakes)
	count=0
	for i in range(number-1):
		if cakes[i]!=cakes[i+1]:
			count+=1
	if cakes[-1]=='-':
		count+=1
	print ('Case #{}: {}'.format(_+1,count))	

