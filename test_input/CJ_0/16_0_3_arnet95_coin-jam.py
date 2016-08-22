from itertools import product

def primes(n):
    correction = (n%6>1)
    n = {0:n,1:n-1,2:n+4,3:n+3,4:n+2,5:n+1}[n%6]
    sieve = [True] * (n/3)
    sieve[0] = False
    for i in xrange(int(n**0.5)/3+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[      ((k*k)/3)      ::2*k]=[False]*((n/6-(k*k)/6-1)/k+1)
        sieve[(k*k+4*k-2*k*(i&1))/3::2*k]=[False]*((n/6-(k*k+4*k-2*k*(i&1))/6-1)/k+1)
    return [2,3] + [3*i+1|1 for i in xrange(1,n/3-correction) if sieve[i]]

poss_jamcoins = []
for seq in product([0,1], repeat=14):
    poss_jamcoins.append([1] + list(seq) + [1])

#Test primality base 2


def f(N, j):
    prime_list = primes(10**4)
    jamcoins = []
    for seq in product([0,1], repeat=N-2):
        l = [1] + list(seq) + [1]
        if len(jamcoins) >= j:
            break
        nums = []
        for base in xrange(2, 11):
            found = False
            for p in prime_list:
                n = sum(l[::-1][i]*base**i for i in xrange(N))
                if n % p == 0:
                    found = True
                    nums.append(p)
                    break
            if not found:
                break
        if len(nums) == 9:
            jamcoins.append([l, nums])

    print "Case #1:"
    for coin, divisors in jamcoins:
        s = "".join([str(i) for i in coin])
        for div in divisors:
            s += " " + str(div)
        print s

f(32, 500)
