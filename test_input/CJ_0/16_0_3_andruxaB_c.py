filename = "/home/andybozhko/Downloads/codejam/C/C-small-attempt0"

def isprime(num):
    flag = (num%2==1)
    m = int(num**0.5)
    i = 3
    while flag and i<=m:
        flag = flag and (num%i!=0)
        i += 2
    return flag

def primeslist():
    plist = [2]
    for i in xrange(3,2**17,2):
        if isprime(i):
            plist += [i]
    return plist
    
with open(filename+"primes.txt","w") as fp:
    fp.write(" ".join(map(str,primeslist())))
    
def isnotprime(num, primeslist):
    flag = False
    div = 1
    for i in primeslist:
        if (int(num**0.5)>=i)and(num%i==0):
            flag=True
            div = i
            break
#    if int(num**0.5)>primeslist[-1]:
#        for i in xrange(primeslist[-1]+2,int(num**0.5)+1,2):
#            if (num%i==0):
#                flag=True
#                div = i
#                break
    return flag, div
    
def convert(num, base):
    digits = []
    while num>0:
        digits += [num%2]
        num = num/2
    digits = [digits[i]*base**i for i in range(len(digits))]
    res = sum(digits)
    return res
    
fp = open(filename+"primes.txt")
plist = map(int, fp.read().split())
fp.close()

fin = open(filename+".in")
fout = open(filename+".out","w")
trials = int(fin.readline())

for T in xrange(trials):
    [N, J] = map(int, fin.readline().split())
    fout.write("Case #{0}:\n".format(T+1))
    
    tot = 0
    for num in xrange(2**(N-1)+1,2**N,2):
        divisors = []
        for j in range(2,10+1):
            f, d = isnotprime(convert(num, j), plist)
            if f:
                divisors += [d]
            else:
                break
        if len(divisors)==9:
            fout.write(str(convert(num,10))+" "+" ".join(map(str,divisors))+"\n")
            tot += 1
        if tot == J:
            break
    
fin.close()
fout.close()