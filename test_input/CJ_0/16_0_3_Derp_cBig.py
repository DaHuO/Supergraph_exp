BASE_LIST = [2,3,4,5,6,7,8,9,10]
PRIME_STORE = dict()
def isNotPrimeTupleWithSmallUpperLimit(n):
	if n in PRIME_STORE.keys():
		return PRIME_STORE[n]		
	if n<2:
		PRIME_STORE[n] =(True,1)
		return (True,1)
	if n==2 or n==3:
		PRIME_STORE[n] = (False,n)
		return (False,n)
	if n%2==0:
		PRIME_STORE[n] = (True,2)
		return (True,2)
	upperLimit = int((n**0.125)+1)
	i = 3
	while (i<upperLimit):
		if n%i==0:
			PRIME_STORE[n] = (True,i)
			return (True,i)
		i+=2
	PRIME_STORE[n] = (False,n)
	return (False,n)

def main():
	testCount = raw_input()
	testCases=list()
	for i in range (0,int(testCount)):
		testCase = raw_input()
		testCases.append(testCase)
	
	for i in range(0,len(testCases)):
		print "Case #"+str(i+1) + ":"
		testCase = testCases[i]		
		params = testCase.split()
		n = int(params[0])
		j = int (params[1])
		printCount = 0
		for v in xrange(0,2**(n-2)):			
			printList = list()
			num = '1'+ '{0:b}'.format(v).zfill(n-2) +'1'			
			printList.append(str(num))
			flag = True
			
			for b in BASE_LIST:
				val = int(num,b)
				divs = isNotPrimeTupleWithSmallUpperLimit(val)				
				isNotPrime = divs[0]
				divVal = divs[1]
			
				if isNotPrime:
					printList.append(str(divVal))
				else:
					flag = False
					break
			
			if flag is True:
				print str(" ".join(printList))
				printCount += 1
			if printCount == j:				
				break
				
if __name__ == '__main__':
	main()