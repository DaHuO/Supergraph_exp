import math
t=int(input())
n,j=map(int,input().split())

print("Case #1:")
'''
def divisorGenerator(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor
'''
def is_prime(n):
    if n == 2 or n == 3: return True,1
    if n < 2 or n%2 == 0: return False,2
    if n < 9: return True,1
    if n%3 == 0: return False,3
    r = int(n**0.5)
    f = 5
    while f <= r:
        #print ('\t',f)
        if n%f == 0: return False,f
        if n%(f+2) == 0: return False,f+2
        f +=6
    return True,1

count=0    
for i in range(32769,65536):
    b=bin(i)[2:]
    
    p=0
    divi=[]
    if count<j:
        if b[0]==b[-1]=='1':
            for k in range(2,11):
                boolval,div=is_prime(int(b,k))
                if not boolval:
                    divi.append(div)
                    p+=1
                if p==9:
                    print(b,end=' ')
                    for l in divi:
                        print(l,end=' ')
                    print()    
                    count+=1
                else:continue
