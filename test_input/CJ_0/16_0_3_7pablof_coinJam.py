import math
def prime(n):
    if n == 2:
        return 0
    if n % 2 == 0 or n <= 1:
        return 2
    ## Whereas limit should be n**0.5 + 1, setting the limit into X will
    ## produce that numbers whose lowest nontrivial divisor is greater than X
    ## will be treated as primes, which will enhance the overall performance
    limit = 10000
    for divisor in range(3, limit, 2):
        if n % divisor == 0:
            return divisor
    return 0

##f = open('test.in')
##f = open('C-small-attempt0.in')
f = open('C-large.in')
f2 = open('file.txt', 'w')
f.readline()
i = 0
for l in f:
    i += 1
    print("Case #" + str(i) + ":", file = f2)
    found = 0
    N, J = [int(x) for x in l.split()]
    for x in range(2**(N-1)+1, 2**N, 2):
        a=''
        coin = bin(x)[2:]
        div = 0
        for base in range(2, 11):
            div = prime(int(coin, base))
            if div == 0:
                break
            a += ' ' + str(div)
        if (div == 0):
            continue
        print(coin + a, file = f2)
        found += 1
        if found == J:
            break
f.close()
f2.close()
