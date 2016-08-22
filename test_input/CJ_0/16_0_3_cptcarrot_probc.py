from math import floor, sqrt

def get_in_base(n, b):
    res = 0
    i = 0
    while n > 0:
        curr = n & 1
        n = n>>1
        res += curr*b**i
        i += 1
    return res

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return 2
    for i in range(3, floor(sqrt(n))+1):
        if n % i == 0:
            return i
    return True

def something(N=16, J=50):
    outfile = open("c-small.out", 'w')
    found = 0
    curr = (1<<(N-1)) + 1
    factor_list = []
    while found < J:
        factors = []
        for base in range(2, 11):
            factor = is_prime(get_in_base(curr, base))
            if factor == True:
                break
            else:
                factors.append(factor)
        if factor != True:
            print('hi')
            binary = format(curr, "0%db" % N)
            outfile.write("%s %s\n" % (binary, ' '.join(map(str, factors))))
            found += 1
            # found.append(format(curr, "0%db" % N))
            # factor_list.append(' '.join(map(str, factors)))
        curr += 2
    outfile.close()
    return found
        
#something()
