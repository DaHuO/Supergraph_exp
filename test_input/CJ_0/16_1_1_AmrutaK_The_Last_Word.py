readFile = open("A-large.in")
testCases = eval(readFile.readline())
ans = {}
for t in range(0,testCases):
    string = readFile.readline()
    temp = string[0]
    for i in range(1,len(string)):
	if string[i] >= temp[0]:
	   temp = string[i] + temp
	else:
           temp = temp + string[i]
    ans[t] = temp

outputFile = open("The_Last_Word_Large.txt",'w')
for i in range(0,len(ans)):
    outputFile.write("Case #%d: %s" % (i+1,ans[i]))

