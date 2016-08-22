# Primes until 100: https://primes.utm.edu/lists/small/1000.txt

PRIMES = [2,
          3,
          5,
          7,
          11,
          13,
          17,
          19,
          23,
          29,
          31,
          37,
          41,
          43,
          47,
          53,
          59,
          61,
          67,
          71,
          73,
          79,
          83,
          89,
          97]

def digits(num):
    ret = []
    while num > 0:
        ret.insert(0, num %10)
        num /= 10

    return ret

def is_jam(num):
    res = []

    for base in xrange(2, 11):
        digits = format(num, 'b')
        num_base = int(digits, base)

        # Test whether we can find a divisor first 100 primes.
        success = False
        for x in PRIMES:
            if num_base % x == 0 and x != num_base:
                res.append(str(x))
                success = True
                break

        if success == False:
            return None

    return res

T = raw_input()

N, J = [int(x) for x in raw_input().split()]

print 'Case #1:'

digs = ['0'] * (N - 2)
digs = ['1'] + digs + ['1']
num = int(''.join(digs), 2)

while J > 0:
    divs = is_jam(num)
    if divs is not None:
        J -= 1
        print format(num, 'b') + ' ' + ' '.join(divs)

    num += 2
