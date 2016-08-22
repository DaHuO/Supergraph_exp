def isPrime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return 2
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return i
    return True
def bases(string):
    for i in range(2,11):
        yield int(string, i)

def genDigits(n):
    length = n-2
    i = 0
    while len(bin(i)) <= length+2:
        yield "1" + bin(i)[2:].zfill(length) + "1"
        i += 1

count = 0
for i in genDigits(4):
    if (count > 11):
        break
    failed = False
    nontrivs = []
    for j in bases(i):
        k = isPrime(j)
        if k==True:
            failed = True
            break
        else:
            nontrivs.append(str(k))
    if not failed:
        print(i, *nontrivs)
        count += 1

