exec open("./prime").read()
exec open("./prime1").read()
primes=l+p
print 'enter'

def isprime(x):
    
    for i in primes:
        if x%i==0:
            if x==i:
                return True
            else:
                return False
    else:
        if x>primes[-1]**2:
            print 'here'#anything greater than square of biggest prime is assumed prime..
            return True
    return True
def get_divisor(x):
    for i in primes:
        if x%i==0:
            return i
t=input()

for _ in xrange(t):
    n,J=map(int,raw_input().strip().split())
    l={i:[] for i in range(2,11)}
    chosen=[]
    i=int('1'+'0'*31,2)
    while i <= 2**n:
        x=bin(i)[2:]
        if len(x)<n or x[-1]=='0':
            i+=1
            continue
        #print 'h'
        for j in l:
            sum=0
            pow=0
            for k in x[::-1]:
                if k=='1':
                    sum+=j**pow
                pow+=1
            l[j].append(sum)
        for j in l:
            if isprime(l[j][-1]):
                break
        else:
            chosen.append(len(l[10])-1)
            print len(chosen)
        if len(chosen)==J:
            break
        i+=1
    for i in chosen:
        print l[10][i],
        for j in sorted(l.keys()):
            print get_divisor(l[j][i]),
        print
                
            
    divisors=[]
    
    #print l[2][:30]
