raw_input()
i=0
while True:
	i=i+1
	nflips=0
	stack=(raw_input().strip())
	if not stack:
		break
	stack=stack.rstrip("+") # Remove pancakes on the bottom which are already + side up
	if len(stack) == 0:
		print "Case #"+str(i)+": 0"
		continue
	while True:
		stack=stack.rstrip("+")
		if len(stack) == 0:
			print "Case #"+str(i)+": "+str(nflips)
			break
		nflips=nflips+1
		# At this point, the bottom of the stack is -
		
		# Case 1: Top of stack is + : Flip the top +'s to -
		if (stack[0]=='+'):
			temp=stack.lstrip("+")
			stack='-'*(len(stack)-len(temp))+temp
		else:
		# Case 2: Top of stack is - : Flip the whole stack and reverse the signs
			stack=stack[::-1]
			stack=stack.replace("+","m")
			stack=stack.replace("-","p")
			stack=stack.replace("m","-") 
			stack=stack.replace("p","+")


