t=int(raw_input())
inputList=[]
for i in xrange(t):
	inputList.append(raw_input())
#print inputList
for i,inp in enumerate(inputList):
	count=0
	lastSwap=inp[0]
	ls=None
	for j in range(1,len(inp)):
		if lastSwap!=inp[j]:
			count+=1
			if lastSwap=='+' and inp[j]=='-':
				lastSwap='-'
			else :
				lastSwap='+'
	if lastSwap=='-':
		count+=1
	print "Case #"+str(i+1)+": "+str(count)