import random

n = 32
m = 500

ans = []
num = 0

def ipow(a,b,n):
    #calculates (a**b)%n via binary exponentiation, yielding itermediate
    #results as Rabin-Miller requires
    A = a = long(a%n)
    yield A
    t = 1L
    while t <= b:
        t <<= 1
    
    #t = 2**k, and t > b
    t >>= 2
    
    while t:
        A = (A * A)%n
        if t & b:
            A = (A * a) % n
        yield A
        t >>= 1

def RabinMillerWitness(test, possible):
    #Using Rabin-Miller witness test, will return True if possible is
    #definitely not prime (composite), False if it may be prime.
    
    return 1 not in ipow(test, possible-1, possible)

def prob_is_composite(possible):
    k = 1000
    for i in xrange(k):
        test = random.randrange(2, possible)|1
        if RabinMillerWitness(test, possible):
            return True
    return False

def get_number(mask, base):

    num = 1

    for i in range(n-3, -1, -1):
        num = num*base + ((mask&(1<<i)) > 0)

    num = num*base + 1

    return num

def is_prime(x):
    i = 2
    while i*i<=x:
        if x%i == 0:
            return False
        i+=1
    return True

def get_div(x):
    i = 2
    while i*i<=x and i < 100000:
        if x%i == 0:
            return i
        i+=1
    return -1

def get_binary(mask):

    s = "1"
    for i in range(n-3, -1, -1):
        if (mask&(1<<i)) > 0:
            s += "1"
        else:
            s += "0"
    s += "1"
    return s

i = 0
while i < (1<<(n-2)):

    if len(ans) >= m:
        break

    found = False

    print i, len(ans)

    for j in range(2, 11, 1):

        if found:
            break

        num = get_number(i, j)

        #print i, j, num

        if not prob_is_composite(num) or get_div(num)<0:
            found = True

    if not found:
        ans.append(i)

    i += 1

file = open("output.txt", "w")
file.write("Case #1:\n")

for x in ans:
    file.write(get_binary(x))
    file.write(" ")
    for j in range(2, 11, +1):
        num = get_number(x, j)
        print x, j, num
        file.write(str(get_div(num)) + " ")
    file.write("\n")

file.close()

