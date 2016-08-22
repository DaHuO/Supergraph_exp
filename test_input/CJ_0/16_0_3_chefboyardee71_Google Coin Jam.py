f = open('Google Coin Jam Small.in','r')
g = open('Google Coin Jam Small.out','w')

def Google_print(filename,answers):
    for i in range(len(answers)):
        filename.write("Case #%s: %s\n" % (str(i+1),answers[i]))
        print "Case #%s: %s" % (str(i+1),answers[i])
    return

def base_k(n,k):
    answer = []
    p = n
    while p:
        r = p%k
        answer.append(str(r))
        p = p/k
    answer.reverse()
    return ''.join(answer)

def base_ten(s,base):
    a = list(s)
    a.reverse()
    answer = 0
    for power in range(len(a)):
        answer += int(a[power])*base**power
    return answer

def sieve(n):
    sieve = [True for i in xrange(n)]
    sieve[0] = False
    sieve[1] = False
    for i in xrange(2,n):
        if not sieve[i]:
            continue
        else:
            j = i**2
            while j<n:
                sieve[j] = False
                j += i
    return sieve

def probably_prime(n):
    global lowprimes
    if n < len(lowprimes):
        if lowprimes[n]:
            return True
        else:
            return False
    if n%2 == 0:
        return False
    #implements Miller_Rabin primality test
    d = n-1
    s = 0
    while d%2 == 0:
        d = d/2
        s += 1
    d = int(d)
    bases = [2,3,5,7,11]
    for a in bases:
        check = 0
        for r in range(s):
            if pow(a,d,n) == 1:
                break
            if pow(a,(2**r*d),n) == n-1:
                break
            check +=1
        if check == s:
            return False
    return True

def next_jamcoin(s):
    n = base_ten(s,2)
    n+=2
    return base_k(n,2)

def is_valid(s):
    for base in range(2,11):
        n = base_ten(s,base)
        if probably_prime(n):
            return False
    return True

def first_divisor(n):
    k = 2
    while k**2 <= n:
        if n%k == 0:
            return k
        if k == 2:
            k += 1
        else:
            k += 2
    return


    

lowprimes = sieve(10**4)
cases = int(f.readline())
N,J = [int(x) for x in f.readline().rstrip().split(' ')]
k = str(10**(N-1)+1)
count = 0
answers = []
while count < J:
    if is_valid(k):
        a = [k]
        for i in range(2,11):
            n = base_ten(k,i)
            d = first_divisor(n)
            a.append(str(d))
        answers.append(' '.join(a))
        count += 1
    k = next_jamcoin(k)
total = ['Case #1:'] + answers
total = '\n'.join(total)
print total
g.write(total)
f.close()
g.close()
    
        


        
            
