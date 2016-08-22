import math



import random
from fractions import gcd

_mrpt_num_trials = 5 # number of bases to test


def is_probable_prime(n):
    assert n >= 2
    # special case 2
    if n == 2:
        return True
    # ensure n is odd
    if n % 2 == 0:
        return False
    # write n-1 as 2**s * d
    # repeatedly try to divide n-1 by 2
    s = 0
    d = n-1
    while True:
        quotient, remainder = divmod(d, 2)
        if remainder == 1:
            break
        s += 1
        d = quotient
    assert(2**s * d == n-1)

    # test the base a to see whether it is a witness for the compositeness of n
    def try_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True # n is definitely composite

    for i in range(_mrpt_num_trials):
        a = random.randrange(2, n)
        if try_composite(a):
            return False

    return True # no base tested showed n as composite


def make_number(base, n):
    n_len = len(str(n)) -1
    number = 0
    for item in str(n):
        number += (int(item) * pow(base, n_len))
        n_len -= 1

    return number


def get_divisor(N):
        if N%2==0:
                return 2
        y,c,m = random.randint(1, N-1),random.randint(1, N-1),random.randint(1, N-1)
        g,r,q = 1,1,1
        while g==1:
                x = y
                for i in range(r):
                        y = ((y*y)%N+c)%N
                k = 0
                while (k<r and g==1):
                        ys = y
                        for i in range(min(m,r-k)):
                                y = ((y*y)%N+c)%N
                                q = q*(abs(x-y))%N
                        g = gcd(q,N)
                        k = k + m
                r = r*2
        if g==N:
                while True:
                        ys = ((ys*ys)%N+c)%N
                        g = gcd(abs(x-ys),N)
                        if g>1:
                                break

        return g

def main():
    f = open("C-small-attempt.in")

    lines = f.readlines()
    case = lines[0].rstrip()
    print("Case #%s:" % case)

    for index in range(1,int(case)+1):
        line = lines[index].rstrip()
        list_item = line.split()

        N = int(list_item[0])
        J = int(list_item[1])
        n1 = N - 2
        n2 = ''
        for i in range(0,int(n1)):
            n2 += '1'

        digit = make_number(2, n2)
        s = bin(digit)
        l = len(s)
        mid = s[2:l]

        result = []
        list_divisor = []
        found_count = 0
        target = make_number(2, mid)
        for i in range(0, target+1):
            if found_count == J:
                break

            result = []
            list_divisor = []
            s = bin(i)
            l = len(s)
            mid = s[2:l]

            dd = ("%0" + str(n1) + "d") % int(mid)

            is_break = False
            t = '1' + str(dd) + '1'
            #print("%s ==> t: %s" % (i,t))
            for ii in range(2, 11):
                mn = make_number(ii, t)
                #print("mn : %s" % mn)
                if is_probable_prime(mn):
                    is_break = True
                    break
                else:
                    result.append(mn)

            if not is_break:
                found_count += 1
                #print("%s , %s ==> r: %s" % (found_count, t,result))
                for r_item in result:
                    list_divisor.append(str(get_divisor(r_item)))
                seq = " ".join(list_divisor)

                print("%s %s" % (t,seq))


        index += 1

    f.close()


main()

