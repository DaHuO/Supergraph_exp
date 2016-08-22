'''
Created on Apr 9, 2016

@author: david
'''

#f=open("exampleC.txt")
#f=open("C-small-attempt0.in")
f=open("C-large.in")

def sieve(n):
    "Return all primes <= n."
    np1 = n + 1
    s = list(range(np1)) # leave off `list()` in Python 2
    s[1] = 0
    sqrtn = int(round(n**0.5))
    for i in range(2, sqrtn + 1): # use `xrange()` in Python 2
        if s[i]:
            # next line:  use `xrange()` in Python 2
            s[i*i: np1: i] = [0] * len(range(i*i, np1, i))
    return list(filter(None, s))

# sqrt(1000000000) = 31622
__primes = sieve(31622)
__primes_set=set(__primes)

def find_div(n):
    if n in __primes_set: return 1
    for p in __primes:
        if n%p == 0: return p
    return 1
    raise "kk"

T=int(f.readline())
P=[]
for i in range(T):
    p = [int(x) for x in f.readline().split()]
    P.append(p)

def gen(n):
    i=0
    n-=2
    while True:
        i+=1
        r = bin(i)[2:]
        if len(r)>n: 
            break
        r = ('0'*n + r)[-n:]
        yield '1'+r+'1'
        
def solve(p):
    n, j = p
    res = []
    for num in gen(n):
        is_all_no_prime = True
        dd = []
        for base in range(2,11):
            v = int(num,base)
            df = find_div(v)
            #print(num, base, v, df)
            if df==1:
                is_all_no_prime = False
                break
            else:
                dd.append(str(df))
                #dd.append("["+str(v)+":"+str(df)+"_"+str(v%df)+"]")
        if is_all_no_prime:
            res.append((num,dd))
            j-=1
            if j == 0:
                break    
    return res
       
fRes = open("res.txt", "w")
case=0
for p in P:
    #print(p)
    case+=1
    sol = solve(p)
    fRes.write("Case #{}:\n".format(case))
    for (k,r) in sol:
        fRes.write("{0} {1}\n".format(k,' '.join(r)))
    #fRes.write("Case #{}: {}\n".format(case,sol))
        
fRes.close()
"""
print(len(list(gen(25))))
for i,v in enumerate(gen(16)):
    print(v)
    if i>10: break
"""