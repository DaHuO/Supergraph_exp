def prime_sieve(n):
    """ Return a list of the primes up to n (inclusive).
    """
    n += 1
    primes = []
    l = [True] * n
    l[0] = l[1] = False
    
    for p in range(2, n):
        if l[p]:
            primes.append(p)
            for i in range(2*p, n, p):
                l[i] = False
    return primes

def get_reps(coin):
    reps = []
    for b in range(2, 11):
        n = 0
        for i in range(len(coin)):
            n += int(str(coin)[-i - 1]) * b ** i
        reps.append(n)
    return reps

#Doesn't fail if all primes in list exhausted
def get_divisors(coin, primes):
    reps = get_reps(coin)
    success = True
    divisors = []
    for r in reps:
        if success:
            for p in primes:
                if p >= r:
                    success = False
                    break
                if r % p == 0:
                    divisors.append(p)
                    break
        else:
            break
    if success and len(divisors) == 9: 
        return("{} {}".format(coin, ' '.join(str(d) for d in divisors)))

def make_coins(N, J):
    num_left = J
    for i in range(2**(N-2)):
        if num_left > 0:
            coin = "1{}1".format(str(bin(i))[2:].zfill(N-2))
            if(get_divisors(coin, primes)):
                num_left-= 1
                print(get_divisors(coin, primes))
        else:
            break

num_cases = int(input())
primes = prime_sieve(100000)

for i in range(num_cases):
    data = input().split()
    N = int(data[0]) # length of jamcoins
    J = int(data[1]) # number of jamcoins

    print("Case #{}:".format(i+1))
    make_coins(N, J)