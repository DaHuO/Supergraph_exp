from itertools import product

fin = open("test.txt",'r')
fout = open("test.out",'w')

GLB_primes = {}

def hasDivisor(n):
    if n in GLB_primes:
        return GLB_primes[n]

    GLB_primes[n] = False

    if n <= 3:
        GLB_primes[n] = False
    elif (n%2==0):
        GLB_primes[n] = 2
    elif (n%3==0):
        GLB_primes[n] = 3
    else:
        i = 5
        while i*i <= n:
            if (n%i==0):
                GLB_primes[n] = i
                break
            elif (n%(i+2)==0):
                GLB_primes[n] = i+2
                break
            i += 6

    return GLB_primes[n]

def interpretBase(s,b):
    sum = 0
    s = s[::-1]

    for i in range(len(s)):
        sum += int(s[i])*(base**i)

    return hasDivisor(sum)
    
combos = list(product(range(2),repeat=14))
jamCoinCount = 0
fout.write("Case #1:\n")
for c in combos:
    if jamCoinCount == 50:
        break
    fullStr = "1"
    for x in c:
        fullStr+= str(x)
    fullStr+="1"
    
    divisorList = [None]*9
    for base in range(2,11):
        res = interpretBase(fullStr,base)

        if res == False:
            break
        else:
            divisorList[base-2]=res

    if divisorList[8] == None:
        continue
    else:
        jamCoinCount += 1
        fout.write(fullStr+" ")
        for i in range(9):
            if i == 8:
                fout.write(str(divisorList[i])+"\n")
            else:
                fout.write(str(divisorList[i])+" ")
        print("Found jamcoin %d." %(jamCoinCount))

fin.close()
fout.close()
        
        
















    

