def openFile(fileName):
    lines = []
    line_number = 0
    with open(fileName, encoding='utf-8') as a_file:
        for a_line in a_file:
            if(line_number!=0):
                lines.append(a_line.rstrip())
            line_number += 1
    return lines

def isPrime(strNum,listOfPrimes):
    num=(int(strNum))    
    ret = 0
    maxComp=0
    
    for i in range(0,len(listOfPrimes)):
        if num%listOfPrimes[i] == 0:
            ret = listOfPrimes[i]
            break
    return ret
        
def formNumber(listOfNumbers):
    
    num=""
    for i in range(0,len(listOfNumbers)):
        num=num+listOfNumbers[i]
    return num

print("Random Generator")
listOfPrimes = [2,3,5]
for i in range(5,10000):
    prime=True
    for j in range(3,round(i/2)+1,2):
        if i%j==0:
            prime=False
    if prime==True:
        print(str(i)+" found")
        listOfPrimes.append(i)
print("End Of Random Generator")        

cases = openFile("C-large.in")
solutions=[]
solutionsDivisors = []
solNum = cases[0].split()[1]
length=cases[0].split()[0]
#Formo el numero
firstNum=["1"]
for i in range(1,int(length)-1):
    firstNum.append("0")
firstNum.append("1")
#print (firstNum)
strNum = ''.join(str(x) for x in firstNum)
#strNum = str(formNumber(firstNum))
#print(strNum)
numFound=0
print(solNum)
while len(solutions)!=int(solNum):
    #print (strNum)
    if strNum[-1]=="1":
        divisors = []
        for i in range(2,11):
            #print(strNum)
            num=int(strNum,i)
            #print(str(num))
            
            div = isPrime(str(num),listOfPrimes)
            divisors.append(str(div))
        if "0" not in divisors:
            solutions.append(strNum)
            solutionsDivisors.append(divisors)
            numFound=numFound+1
            #print (strNum)
            #print(str(numFound)+" found")
            
    strNum = str(bin(int(strNum,2)+1))
    strNum = strNum[2:]
#print(solutions)
#print(solutionsDivisors)
for i in range(0,len(solutions)):
    line=solutions[i]
    for j in range(0,len(solutionsDivisors[i])):
        line = line+" "+solutionsDivisors[i][j]
    print(line)
    
            
