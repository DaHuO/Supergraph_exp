import math
import itertools
import sys,time

def divisorGenerator(n):
    large_divisors = []
    for i in xrange(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

T=input()
sys.stdout.flush()
while(T>0):
    N=input()
    J=input()
    a=["".join(seq) for seq in itertools.product("01",repeat=N-2)]
    count=0
    #print "len %d" %len(a)
    print "Case #%d:" %T
    for i in range(len(a)):
        if(count<J):
            number=int('1'+a[i]+'1')
            base2=int(str(number),2)
            base2bool=is_prime(base2)
            #divisor2=list(divisorGenerator(base2))[1]

            base3=int(str(number),3)
            base3bool=is_prime(base3)
    	
            base4=int(str(number),4)
            base4bool=is_prime(base4)

            base5=int(str(number),5)
            base5bool=is_prime(base5)

            base6=int(str(number),6)
            base6bool=is_prime(base6)

            base7=int(str(number),7)
            base7bool=is_prime(base7)
    
            base8=int(str(number),8)
            base8bool=is_prime(base8)

            base9=int(str(number),9)
            base9bool=is_prime(base9)

            base10=int(str(number),10)
            base10bool=is_prime(base10)

            finalbool=(base2bool or base3bool or base4bool or base5bool or base6bool or base7bool or base8bool or base9bool or base10bool)
            if(finalbool==False):
                count=count+1
                print "%d %d %d %d %d %d %d %d %d %d" %(number,list(divisorGenerator(base2))[1],list(divisorGenerator(base3))[1],list(divisorGenerator(base4))[1],list(divisorGenerator(base5))[1],list(divisorGenerator(base6))[1],list(divisorGenerator(base7))[1],list(divisorGenerator(base8))[1],list(divisorGenerator(base9))[1],list(divisorGenerator(base10))[1])
        else:
            break
    T=T-1
