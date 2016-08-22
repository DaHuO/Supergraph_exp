# def isPrime(n):
#     global divisor
#     if n < 2:
#         return False

#     if n == 2:
#         return True

#     for i in range(2, n ** 1/2) :
#         if n % i == 0:
#             divisor = i
#             return False

#     return True

def isPrime2(n):
    global divisor
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0:
        divisor = 2
        return False
    elif n % 3 == 0:
        divisor = 3
        return False
    x = 5
    while x * x <= n:
        if n % x == 0:
            divisor = x
            return False
        elif n % (x + 2) == 0:
            divisor = x + 2
            return False
        x += 6
    return True

t = int(raw_input())
for i in xrange(1, t + 1):
    line = raw_input().split(" ")
    n = int(line[0])
    j = int(line[1])
    lower_bound = 2 ** (n-1) + 1
    # upper_bound = 2 ** n - 1

    print "Case #{}:".format(i)

    k = lower_bound
    while True:
        bin_str = bin(k)[2:]

        # print bin_str

        if bin_str[-1] != '1':
            k += 1
            continue

        res = []
        for b in xrange(2, 11):
            value_base = int(bin_str, base=b)
            if not isPrime2(value_base):
                res.append(str(divisor))
            else:
                break
        if len(res) == 9:
            print "{} {}".format(bin_str, " ".join(res))
            j -= 1
            if j == 0:
                break

        k += 1
        













