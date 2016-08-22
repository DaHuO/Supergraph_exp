import math

fout = open('c.out', 'w')
fin = open('C-small-attempt1.in', 'r')

primes = [2]

def genPrimes():
    for x in range(3, 131072):
        isPrime = True
        for y in primes:
            if x % y == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(x)

def findDivisor(num):
    bound = math.sqrt(num)
    for x in primes:
        if bound < x:
            break
        if num % x == 0:
            return x
    return -1

def asNBase(num, n):
    total = 0
    for idx, val in enumerate(reversed(list(num))):
        if val == 1:
            total += pow(n,idx)
    return total

def toBinaryArray(num):
    arr = []
    while num > 0:
        arr.append(num%2)
        num //= 2
    return list(reversed(arr))
#print(asNBase(toBinaryArray(9), 4))
#quit()

genPrimes()

t = int(fin.readline())
for x in range(1,t+1):
    s = fin.readline().split(' ')
    n = int(s[0])
    j = int(s[1])
    num = pow(2,n-1) + 1
    count = 0
    fout.write('Case #{}: \n'.format(x))
    while count < j:
        answers = []
        for b in range(2,11):
            d = findDivisor(asNBase(toBinaryArray(num),b))
            if d < 0:
                break
            answers.append(d)
        if len(answers) == 9:
            count += 1
            fout.write(''.join(str(e) for e in toBinaryArray(num)))
            for a in answers:
                fout.write(' {}'.format(a))
            fout.write('\n')
        num += 2
