import math
def divisorGenerator(n):
    large_divisors = []
    for i in xrange(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor

from math import sqrt

def mrange(start, stop, step):
    while start < stop:
        yield start
        start += step

def is_prime(num):
    if num == 2:
        return True
    if (num < 2) or (num % 2 == 0):
        return False
    return all(num % i for i in mrange(3, int(sqrt(num)) + 1, 2))

t=int(raw_input())
st=raw_input()
ls=st.split(" ")
length=int(ls[0])
cases=int(ls[1])
n=length*str(1)
#print n
max=int(n,2)
#print max
min=0
outcntr=cases
outp=""
print("Case #1:")
for i in range(0,max+1):
    #print outcntr
    bny=str(int(bin(i)[2:]))
    bnylen=int(len(bny))
    #outp=bny+" "
    if bnylen==length and bny[0]=="1" and bny[bnylen-1]=="1":
        #print "i =",i
        #print bny

        noprimels=[]
        for j in range(2,11):
            chekprm=int(bny,j)
            #print "chek ",chekprm
            if is_prime(chekprm):
                break
            else:
                noprimels=noprimels+[chekprm]

        if len(noprimels)==9:
            dvls=[]
            for x in range(0,9):
                #print noprimels[x]
                templs=list(divisorGenerator(noprimels[x]))

                dvls=dvls+[templs[1]]
            if outcntr>0:
                printoutstmt=bny+" "+str(dvls[0])+" "+str(dvls[1])+" "+str(dvls[2])+" "+str(dvls[3])+" "+str(dvls[4])+" "+str(dvls[5])+" "+str(dvls[6])+" "+str(dvls[7])+" "+str(dvls[8])
                print(printoutstmt)
                #print(bny,dvls)
                outcntr=outcntr-1
            else:
                break

