import sys, math, itertools

def prime_divisor(num):
    if num == 2:
        return True
    if num % 2 == 0:
        return 2

    for i in range(3, math.floor(num**.5+1), 2):
        if num % i == 0:
            return i
    return -1

# A jamcoin is a string of N ≥ 2 digits with the following properties:
# Every digit is either 0 or 1.
# The first digit is 1 and the last digit is 1.
# If you interpret the string in any base between 2 and 10, inclusive, the resulting number is not prime.
def is_valid(jamcoin):
    if jamcoin[0] == '0' or jamcoin[-1] == '0':
        return []

    divisors = []
    for i in range(2,11):
        n = int(jamcoin, i)
        d = prime_divisor(n)
        if d == -1:
            return []
        else:
            divisors.append(d)

    return divisors

def gen_coins(l):
    for seq in itertools.product('01', repeat=l-2):
        coinstr = '1' + ''.join(seq) + '1'
        divisors = is_valid(coinstr)
        if len(divisors) == 9:
            divstr = ' '.join(map(str, divisors))
            yield "{} {}".format(coinstr, divstr)

infile = sys.argv[1]
outfile = sys.argv[2]

with open(infile) as inf:
    with open(outfile, 'w') as outf:
        test_case = 1
        t = inf.readline()
        for line in inf.readlines():

            tokens = line.split(' ')
            n, j = int(tokens[0]), int(tokens[1])

            outf.write("Case #{}:".format(test_case) )

            gen = gen_coins(n)
            for i in range(j):
                coin = gen.__next__()
                outf.write('\n'+coin)

            test_case += 1
