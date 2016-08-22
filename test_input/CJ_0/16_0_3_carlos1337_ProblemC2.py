'''
Created on Apr 8, 2016

@author: Carlos
'''
def jamcoin(num,tam):
    return "1"+bin(num)[2:].rjust(tam,'0')+"1"

def is_legitimate(coin):
    divisores = []
    for i in range(2,11):
        numero = ToBase(coin,i)        
        divisor = -1
        for prime in reversed(prime_list):
            if numero % prime ==0:
                divisor = prime
                break        
        if(divisor < 0 or divisor ==numero):            
            return None
        else:
            divisores.append(str(divisor))
    return divisores

def ToBase(str,base):
    num = 0
    for c in str:
        num*=base
        if c=='1':
            num+=1
    return num

upper_limit = 2**8
upper_limit2 = upper_limit**2
primes = [True]*(upper_limit2)
for i in range(2,upper_limit):
    for j in range(2*i,upper_limit2,i):
        if(j < upper_limit2):
            primes[j]=False
            
prime_list = []
for i in range(2,upper_limit2):
    if(primes[i]):
        prime_list.append(i)

print(is_legitimate("1001"))

f = open('C-large.in','r')
f2 = open('C-large.out','w')
 
f.readline()
N,J = f.readline().split(" ")
num = 0
f2.write("Case #1:\n")
for i in range(int(J)):
    found = False
    while(not found):
        coin = jamcoin(num,int(N)-2)
        divisores = is_legitimate(coin)
        if divisores is not None :
            found=True
            f2.write(coin+" "+" ".join(divisores)+"\n")
        num+=1

