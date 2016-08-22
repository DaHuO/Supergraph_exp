def isprime(n):
    """Returns True if n is prime."""
    if n == 2 or n == 3:
        return True, -1
    if n % 2 == 0:
        return False, n // 2
    if n % 3 == 0:
        return False, n // 3

    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False, i

        i += w
        w = 6 - w
    return True, -1

def jamCoin(l, j):
    x = -1
    count = 0
    val = 0
    while count < j:
        x += 1
        divisor = []
        discard = False
        bix = bin(x)[2:]
        for base in range(2, 11):
            val = 1 + base**(l-1) + base * ( int(bix, base) )
            prime, valp = isprime(val)
            if not prime:
                divisor.append(valp)
            else:
                discard = True
                break
        if discard:
            continue
        else:
            val = 1 + 2**(l-1) + 2*(int(bix, 2))
            res = ""
            for div in divisor:
                res += " " + str(div)
            print( bin(val)[2:] + " " + res )
            count += 1

t = int(input())
for i in range(1, t+1):
    L, J = input().split(' ')
    print("Case #"+str(i)+":")
    jamCoin(int(L), int(J))
