

def process(stack):
	#stack=stack+"+"
	cost=0
	index=0
	firstIncidet=True
	print stack
	#for i in range(len(stack)):
	while index<len(stack):
		while (stack[index]=="-"):
			index+=1
			if (index <= len(stack)):
				break
		if stack[0]=="-" and firstIncidet:
			cost+=1
			firstIncidet=False
		else:
			cost+=2
		
		if index>=len(stack):
			break


		#print str(len(stack))+" *** "+str(index)+" *** "+stack[index]
		while (stack[index]=="+"):
			index+=1
			if  (index <= len(stack)):
				break


	print cost
	return cost


def nazi(stack):
	stack=stack+"+"
	cost=0
	for i in range(len(stack)-1):
		if stack[i]=="-" and stack[i+1]=="+":
			cost+=2

	if stack[0]=="-":
		cost=cost-1

	#print cost
	return cost



def main():
	index=0
	with open("B-large.in", "r") as ins:
		numOfTestCases=int(ins.readline())
		#print "#cases "+str(numOfTestCases)
		

		cases=[]
		for i in range(numOfTestCases):
			stack=str(ins.readline().rstrip())
			
			flip=nazi(stack)
			print "Case #"+str(i+1)+": "+str(flip)
			#break



main()