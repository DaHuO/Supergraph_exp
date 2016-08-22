readFile = open("B-large.in")
testCases = eval(readFile.readline())
ans = {}
for t in range(0,testCases):
    string = readFile.readline()
    #Left to right string 
    stack = []
    #Left bottom of stack right top of stack
    for i in range(len(string)-1,-1,-1):
        if string[i] == '+':
           stack.append(1)
	if string[i] == '-':
           stack.append(0)
    flips = 0
    while 0 in stack:
	i = len(stack)-1
	queue = []
	while stack[i] == stack[i-1] and i > 0:
	      queue.append(stack[i] ^ 1)
	      del stack[i]
	      i -= 1
	queue.append(stack[i] ^ 1)
        del stack[i]
	for j in range(0,len(queue)):
	    stack.append(queue[j])	
        flips += 1
    ans[t] = flips

outputFile = open("Pancakes_output.txt",'w')
for i in range(0,len(ans)):
    outputFile.write("Case #%d: %s\n" % (i+1,ans[i]))

