DONE = 0

def isprobableprime(n, k = 999):
    if n <= k:
        k = n-1
    
    if n % 2 == 0:
        return False, 2

    for i in range(3,k+1,2):
        if n % i == 0:
            return False, i
    return True, -1

def check(v):
    divs = [0]*9
    for i in range(2,len(v)):
        res, divs[i-2] = isprobableprime(v[i])
        if res:
            return False, []
    return True, divs

def rec(v,n,N,s,J):
    global DONE 

    if DONE==J:
        return

    if n == N-1:
        res, divs = check(v)
        if res:
            DONE += 1
            print("%s %s" % (''.join([str(i) for i in s]), ' '.join([str(i) for i in divs])))
        return

    rec(v[::],n+1,N,s[::],J)
    for i in range(2,11):
        v[i] += i**(n)
    s[-n-1]=1
    rec(v[::],n+1,N,s[::],J)

def solve():
    N,J = [int(i) for i in input().split()]
    v = [0]*11
    for i in range(2,11):
        v[i] = (i**(N-1))+1
    s = [0]*N
    s[0]=1
    s[-1]=1
    rec(v[::],1,N,s[::],J)
    return

T = int(input())
for t in range(1,T+1):
    print("Case #%d:" % (t))
    solve()
