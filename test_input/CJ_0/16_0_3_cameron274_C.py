def convert_base(n, base):
    #takes a "binary" string and converts it to a different base
    result = 0
    b = 1
    while (n != 0):
        result += (n % 10) * b
        n //= 10
        b *= base
    return result

def find_factor(n):
    #returns a nontrivial divisor, or None if there aren't any
    if (n == 2): return None
    if (n % 2 == 0): return 2
    k = 3
    limit = n**(.5)
    while (k <= limit):
        if (n % k == 0): return k
        k += 2
    return None

def run_test():
    params = raw_input().split(" ")
    N = int(params[0])
    J = int(params[1])
    test = 2**(N-1) + 1
    found = 0
    factors = [None] * 9
    while (found < J):
        jamcoin = int(bin(test)[2:])
        is_jamcoin = True
        for base in range(2, 11):
            n = convert_base(jamcoin, base)
            k = find_factor(n)
            if (k == None):
                is_jamcoin = False
                break
            else:
                factors[base-2] = k
        if is_jamcoin:
            found += 1
            print("%d %d %d %d %d %d %d %d %d %d" % (jamcoin, factors[0],
                factors[1], factors[2], factors[3], factors[4],
                factors[5], factors[6], factors[7], factors[8]))
        test += 2

t = int(raw_input())
print("Case #%d:" % t)
run_test()