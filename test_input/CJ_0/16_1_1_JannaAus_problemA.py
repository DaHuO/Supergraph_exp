import time

def convertString(a, b):
	if (a[0] <= b):
		return b + a
	return a + b

start_time = time.time()

# f = open("sample1A.txt")
f = open("A-large01.in")
# f = open("B-large.in")
result = open('A-large01.in.txt', 'w')
# result = open('B-large-output.txt', 'w')

cases = int(f.readline().rstrip())
for x in xrange(0, cases):
	inStack = list(f.readline().rstrip())
	outStack = reduce(lambda a, b: convertString(a,b), inStack)
	caseResult = "Case #"+str(x+1)+": " + outStack + "\n"
	# print outStack
	# print caseResult
	result.write(caseResult)
f.close()
result.close()

print("--- %s seconds ---" % (time.time() - start_time))

