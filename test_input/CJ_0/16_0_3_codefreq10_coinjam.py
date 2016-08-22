#t=raw_input()
#l=raw_input()
import itertools
N=16
J=50
count=0
fp=open("preinp","r")
inputList=[]
'''def isPrime(a):
	print a
	if pow(2,a-1)%i==1:
		return True
	else:
		return False'''
def isPrime(n):
    """Returns True if n is prime."""
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True
def getAFactor(num):
	#print "num",num
	#print "Divide",num//2
	for b in itertools.count(1):
	#for i in xrange(2,num//2+2):
		if b==1 or b==0:
			continue
		if num%b==0:
			return b
for i in range(0,16384):
	inputList.append(fp.readline())
#print inputList
for i,inp in enumerate(inputList):
	if '\n' in inp:
		inputList[i]=inp[0:inp.index('\n')]
#print inputList
print "Case #1:"
count=0
'''for i,inp in enumerate(inputList):
	for b in range(2,11):
		print int(inp,b)'''
for i,inp in enumerate(inputList):
	if i==len(inputList)-1:
		break
	flag=False
	for b in range(2,11):
		num=int(inp,b)
		if isPrime(num):
			flag=True
			break
	if flag==True:
		continue
	#print "Number through",inp
	factors=[]
	count+=1
	for b in range(2,11):
		num=int(inp,b)
		fac=getAFactor(num)
		factors.append(fac)
	res=""
	for i in factors:
		res=res+str(i)+" "
	print inp+" "+res
	if count==J:
		break