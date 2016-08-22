T = input()

n, j = map(int, raw_input().split(' '))

b = int('1000000000000001', 2)
e = int('1111111111111111', 2)
cnt = 0

def getDivisor(num_str, base):
    import math
    num = int(num_str, base)
    if num % 2 == 0:
        return 2
    i = 3
    sqrt = math.sqrt(num)
    while i < sqrt:
        if num % i == 0:
            return i
        i += 2
    return 0


def getDivisors(bs):
    divs = []
    for base in xrange(2, 11):
        d = getDivisor(bs, base)
        if d > 0:
            divs.append(d)
        else:
            return []
    return divs


for num in range(b, e+1):
    # check num is not prime for all bases 2 - 10
    # print the list of non-trivial divisors for each base
    s = bin(num)[2:]
    lst = []
    if s[0] == s[n-1] == '1':
        lst = getDivisors(s)

    if lst:
        print s,
        for x in lst:
            print x,
        print
        cnt += 1
    if cnt == j:
        break
