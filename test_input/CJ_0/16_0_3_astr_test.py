import collections
import math
# debug=False
# with open('B-small-attempt1.in') as f:
# debug=True
with open('C-small-attempt1.in') as f:
	content = f.readlines()


def getDevisor(num):
	if num % 2 == 0:
		return str(2)
	for x in range(3,int(math.sqrt(num))+1,2):
		if(num%x==0):
			return str(x)		
	return 0

def isJamPoint(number,devisorList):
	baseSet={2,3,4,5,6,7,8,9,10}
	for base in baseSet:
		newNum=int(number,base)
		devisor=getDevisor(newNum)
		if(devisor==0):
			return False
		else:
			devisorList.append(devisor)
	return True

def generateNewNumber(number):
	# print("number:(generateNewNumber) "+number)
	lst=list(number)
	for x in range(len(lst)-2,0,-1):
		if(lst[x]=="0"):
			lst[x]="1"
			# print("lst: "+str(lst))
			return "".join(lst)
		else:
			lst[x]="0"

def	printNumberAndDevisors(number,devisorList):
	print(number+" "+ " ".join(devisorList))

def printJamCoinWithDevisor(N,J):
	number="1"+("0"*(N-2))+"1"
	while J>0:
		# print("J: "+str(J))
		devisorList=[]
		if(isJamPoint(number,devisorList)):
			printNumberAndDevisors(number,devisorList)
		else:	
			J+=1
		number=generateNewNumber(number)
		J-=1

numOfTestCase=int(content.pop(0))
for x in range(numOfTestCase):
	N,J=[int(v) for v in content.pop(0).split()]
	# print("N: "+str(N))
	print("Case #%d: "%(x+1))
	printJamCoinWithDevisor(N,J)

