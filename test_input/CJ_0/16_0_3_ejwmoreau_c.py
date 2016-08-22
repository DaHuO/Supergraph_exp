from math import sqrt

def is_prime(string):
    factors = []
    prime = True
    for base in range(2, 11):
        num = int(string, base)
        limit = int(sqrt(num)) + 1
        for n in range(3, limit):
            if num % n == 0:
                factors.append(str(n))
                prime = False
                break
        if prime:
            #print("%s is a prime" % string)
            return []
        prime = True
    #print("%s is divisible by %s" % (string, factors))
    return factors

print("Case #1:")
input()
n, j = input().strip().split()
n, j = int(n), int(j)

curr_j = 1
for num in range(2 ** (n - 2)):
    formatStr = '{0:0%sb}' % (n - 2)
    string = '1' + formatStr.format(num) + '1'

    factors = is_prime(string)
    if len(factors) == 0:
        continue

    print(string, " ".join(factors))

    if curr_j == j:
        break
    curr_j += 1
