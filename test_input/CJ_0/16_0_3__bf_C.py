
def intToBin(x, n):
    dec = 0
    
    b = 1 << n
    while b > 0:
        dec *= 10
        if b & x:
            dec += 1
        b >>= 1
        
    return dec


def base(x, b):
    xb = 0
    p = 1
    while x > 0:
        q = x%10
        xb += (q*p)
        p *= b
        x /= 10
        
    return xb
    
def notPrime(x):
    for i in range(2, 11):
        xb = base(x, i)
        
        prime = True
        #for k in (2, 3, 5, 7, 11):
        for k in range(2, 101):
            if xb % k == 0:
                prime = False
                break 
        
        if prime == True:
            return False
            
    return True


def div(x, b):
    xb = base(x, b)
    
    #for k in (2, 3, 5, 7, 11):
    for k in range(2, 101):
        if xb % k == 0:
            return k
            
    return 0
    

n = 32
j = 500

x = 1
for i in range(0, n-1):
    x *= 10
x += 1

print "Case #1: "
    
i = 0
tot = 0
while tot < j and i < 1073741824:

    xmid = intToBin(i, n) * 10
    xsum = x + xmid
    
    pr = []
    if notPrime(xsum):
        pr.append(xsum)
        for k in range(2, 11):
            pr.append(div(xsum, k))
        pr.append('\n')
        
        for p in pr:
            print p,
                
        tot += 1

    i += 1
