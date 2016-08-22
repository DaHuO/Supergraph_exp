# adapted from rosetta code
def prime(a):
    if a < 2: return (False, 1)
    if a == 2 or a == 3: return (True, a) # manually test 2 and 3   
    if a % 2 == 0: return (False, 2)
    if a % 3 == 0: return (False, 3)
    maxDivisor = a**0.5
    d, i = 5, 2
    while d <= maxDivisor:
        if a % d == 0: return (False, d)
        d += i 
        i = 6 - i # this modifies 2 into 4 and viceversa
    return (True, a)

t = int(raw_input())
for case in range(1, t+1):
    print "Case #%d:" % case
    n, j = map(int, raw_input().split(" "))
    m = 2**(n-2) # n-2 because we don't need first or last digits,
    num_found = 0
    for candidate in xrange(m):
        sums = {}
        for base in range(2, 10+1): # our very specific bounds!
            sum = 1 # last digit is 1
            x = candidate
            i = 1
            while x > 0:
                sum += (x % 2) * (base ** i)
                x /= 2
                i += 1
            sum += base ** (n-1) # first digit is 1
            (is_prime, divisor) = prime(sum)
            if is_prime:
                break
            sums[base] = (sum, divisor)
        else: # for/else????
            print "1" + bin(candidate)[2:].zfill(n-2) + "1",
            for base in range(2, 10+1):
                print sums[base][1],
            print ""
            num_found += 1
            if num_found == j:
                break

