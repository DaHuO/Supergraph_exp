import math

def isPrime(n):
    if (n<2 or ((n&1)==0 and n!=2)):
        return 2
    
    for i in range(3,min(100,math.floor(math.sqrt(n))+1),2):
        if ((n%i)==0):
            return i
    return 0

def base(a, b) :
    res = 0
    bs = 1
    for i in range(0,32):
        if (a&(1 << i)):
            res = res + bs
        bs = bs*b
    return res

def cal( k) :
    i=0
    while(True):
        for i in range(2,12):
            if (i == 11):
                return k
            if (isPrime(base(k, i))==0):
                break
        k=k+2;


n=500
i = 1
fpo = open("output.txt", "w");
fpo.writelines("Case #1:\n");

r = 0x80000001
while (n) :
    print(n)
    r = cal(r);
    fpo.writelines(str(base(r,10)))
    for i in range(2,11):
        fpo.writelines(' '+str(isPrime(base(r, i))))    
    fpo.writelines('\n')
    r = r + 2;
    n=n-1
fpo.close()


