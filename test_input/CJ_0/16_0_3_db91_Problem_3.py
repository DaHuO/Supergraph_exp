import random
import math
import time
start_time = time.time()

primeSet=set([2,3,5,7])
iput = []
i = 0
line = 0
output = []


def generateRand(leng):
    strTest = "1"
    leng -= 2
    while leng > 0:
        strTest += str(random.randint(0, 1))
        leng -= 1
    strTest += "1"
    return strTest


def generateBase(power, val):

    toreturn = 0

    for k in range(0, len(val)):
        toreturn += math.pow(int(power), k) * int(val[len(val) - 1 - k])
    return toreturn


with open('op.txt', 'r') as f:
    iput.append(f.read())

iput = iput[0].split("\n")
iput = iput[1:len(iput)]



def checkPrime(num1):

    num=int(num1)
    divisor=[]
    #print primeSet
    #for k7 in primeSet:
    if (num%2==0):
      #print "returning"
      return True, 2

    i=3
    #print primeSet
    while(i<int(math.sqrt(num))):
        if num%i!=0:
            i=i+2
        elif num%i == 0:
            #if(i in primeSet):
                #print "present"+str(i)
            #primeSet.add(i)
            #print primeSet
            return True,i
    return False,0
t=1

for x in iput:
    j = x.split(" ")
    numCases=1
    numList=[]
    numNotPrimeList=[]
    finallist=[[]]
    print "Case #"+str(t)+":"
    while(numCases<int(j[1])+1):
        num = generateRand(int(j[0]))
        divisor = ""
        flag = 0
        #print num

        if(num not in numList):
            numList.append(num)
            for k2 in range(2,11):
                cond,vl3=checkPrime(str(int((generateBase(k2, num)))))
                #print "k"
                if(cond==True):
                    flag=flag+1
                    divisor=divisor+str(vl3)+" "


            if flag==9:

                print str(num)+" "+divisor
                numCases+=1
                numNotPrimeList.append(num)
                divisor=divisor[0:len(divisor)-1]

                divisor=""
    t=t+1
    #print numNotPrimeList

#print  primeSet
#print max(primeSet)
#print("--- %s seconds ---" % (time.time() - start_time))
