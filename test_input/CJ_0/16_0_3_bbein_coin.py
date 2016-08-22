import math as m

def gen_n(N):
    for i in range(2):
        if i == 0:
            s='0'
        else:
            s='1'
        if N >1:
            for char in gen_n(N-1):
                yield s+char
        else:
            yield s

def is_prime(number, primes):
    s = int(m.sqrt(number))
    for x in primes:
        if number%x ==0:
            return False
        if x > s:
            return True
    for x in range(primes[-1]+1,s):
        if number%x ==0:
            return False
    return True    

def add_primes(primes,number):
    j = 0
    for i in range(primes[-1]+1, number):
        if is_prime(i,primes):
            primes.append(i)
            j+=1
        if j > 100:
            return False
    primes.append(number)
def is_not_prime(number,primes):
    s = int(m.sqrt(number))
    for x in primes: 
        if number%x ==0:
            return x
        if x > s:
            if number > primes[-1]:
                add_primes(primes,number)
            break
    for x in range(primes[-1]+1,s):
        if number%x ==0:
            return x
    add_primes(primes,number)
    return 0
    
                
f = open("C-small-attempt0.in", 'r') #opens a file at the beginning
line=f.readline() #reads the next line of the file (until next \n)
T=int(line)
primes = [2,3]
for t in range(T):
    line=f.readline() #reads the next line of the file (until next \n)
    line = line.split(' ')
    N, J=int(line[0]), int(line[1])
    j=0
    answers=[]
    for c in gen_n(N-2):
        coin = "1"+c+"1"
        answer = coin
        add = True
        for i in range(2,11):
            p = is_not_prime(int(coin,i),primes) 
            if p == 0:
                add = False
                break
            answer += " "+str(p)
        if add:
            j+=1
            answers.append(answer)    
        if j == J:
            break
    print('Case #'+str(t+1)+':')
    for answer in answers:
        print(answer)
#print(primes)
#print(len(primes))        