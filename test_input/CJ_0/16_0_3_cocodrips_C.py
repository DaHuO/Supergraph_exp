import copy


def solve(n, j):
    jamcoins = []
    for i in xrange((1 << n - 1) + 1, 1 << (n), 2):
        divisors = []
        for base in xrange(2, 11):
            sum = 0
            index = 0
            while (i >> index) > 0:
                tmp = i >> index
                if tmp & 1:
                    sum += base ** index
                index += 1
            
            divisor = is_prime(sum)
            if divisor == -1:
                break
            # print bin(i), base, sum, divisor
            divisors.append(str(divisor))
            
        else:
            jamcoins.append((bin(i)[2:], copy.deepcopy(divisors)))
        
        if len(jamcoins) == j:
            return jamcoins

def is_prime(n):
    i = 2
    while i * i < n:
        if n % i == 0:
            return i
        i += 1
    return -1


t = int(raw_input())
for i in xrange(t):
    n, j = map(int, raw_input().split())
    jamcoins = solve(n, j)
    print "Case #1:"
    for num, divisors in jamcoins:
        print "{} {}".format(num, ' '.join(divisors))
        


