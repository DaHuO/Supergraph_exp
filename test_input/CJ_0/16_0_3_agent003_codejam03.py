from math import sqrt; from itertools import count, islice
fout = open(r"C:\Users\Ekansh\Downloads\output34.txt","w")
def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

def isjamcoin(n):
    for i in range(2,11):
        if isPrime(int(n,i)):
            return False
    return True
def printdivisor(num):
    temp = num
    for i in range(2,11):
        n = int(num,i)
        for j in range(2,n):
            if n%j==0:
                temp = temp + " " + str(j)
                break
    fout.write(temp)
    fout.write("\n")
        
fobj = open(r"C:\Users\Ekansh\Downloads\C-small-attempt0.in")

n1 = 0
for line in fobj:
    n1 = line.rstrip()
    break
n1 = int(n1)
for i in range(n1):
    fout.write(str("Case #"+str(i+1)+":\n"))
    n=0
    j=0
    for line in fobj:
        a = line.rstrip()
        n,j = a.split(" ")
        break
    n = int(n)
    j = int(j)
    l = 2**(n-2)
    a = []
    for i in range(l):
        p = bin(i)[2:]
        while(len(p) < n-2):
            p = "0"+p
        p = "1"+p+"1"
        a.append(p)
    for num in a:
        if(j == 0):
            break
        if(isjamcoin(num)):
            j -= 1
            printdivisor(num)

fobj.close()
fout.close()

