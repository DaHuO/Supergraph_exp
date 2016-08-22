

import math

the_prime_list = [2,3,5]

def gen_prime_list(max_num):
    targetsqrt =  math.sqrt(max_num)
    cad = the_prime_list[len(the_prime_list)-1]
    while the_prime_list[len(the_prime_list)-1] < targetsqrt:
        isPrime = 1
        for divider in the_prime_list:
            if cad % divider == 0:
                isPrime = 0
                break
        if isPrime:
            the_prime_list.append(cad)
        cad+=1


def the_is_prime(number):
    thesqrt = math.sqrt(number)
    isPrime = 1
    for divider in the_prime_list:
        if divider > thesqrt:
            break
        if number % divider == 0:
            isPrime = 0
            break
    if isPrime:
        return 0
    else:
        return divider

# N = 14
def int_to_coinjam_list(value, N):
    rlist = [0 for x in range(N)]
    idx = 0
    while value:
        rlist[idx] = value & 1
        value = value >> 1
        idx +=1
    rlist.reverse()
    return rlist


def genValue(N, base):
    value = 1
    for iter in range(len(N)):
        value = base*value + N[iter]

    value = base * value + 1
    return value

# N
def find_coin_jam(N,J):
    # loop and find
    found = 0;
    start = -1

    while found < J:
        start += 1
        sample = int_to_coinjam_list(start, N-2)

        v2 = genValue(sample, 2)
        v3 = genValue(sample, 3)
        v4 = genValue(sample, 4)
        v5 = genValue(sample, 5)
        v6 = genValue(sample, 6)
        v7 = genValue(sample, 7)
        v8 = genValue(sample, 8)
        v9 = genValue(sample, 9)
        v10 = genValue(sample, 10)
        #print(sample)
        #print(start)
        #print(v3)
        # print(sample)
        d2 = the_is_prime(v2)
        #print(d2)
        if d2 == 0:
            continue;
        d3 = the_is_prime(v3)
        #print(d3)
        if d3 == 0:
            continue;

        d4 = the_is_prime(v4)
        if d4 == 0:
            continue;

        d5 = the_is_prime(v5)
        if d5 == 0:
            continue;

        d6 = the_is_prime(v6)
        if d6 == 0:
            continue;

        d7 = the_is_prime(v7)
        if d7 == 0:
            continue;

        d8 = the_is_prime(v8)
        if d8 == 0:
            continue;

        d9 = the_is_prime(v9)
        if d9 == 0:
            continue;

        d10 = the_is_prime(v10)
        if d10 == 0:
            continue;
        found +=1
        #print "Found"
        #print(v2,v3,v4,v5,v6,v7,v8,v9,v10)
        print "1{0}1 {1} {2} {3} {4} {5} {6} {7} {8} {9}    ".format("".join(str(x) for x in sample),
                                                                  d2,d3,d4,d5,d6,d7,d8,d9,d10)
        #print (found)
        #print (sample)

        d2 = the_is_prime(v2)
        if d2 == 0:
            continue;



gen_prime_list(10000000000)

print ("Case #1:")
#find_coin_jam(16,50)
#find_coin_jam(6,3)
#find_coin_jam(16,50)
find_coin_jam(32,500)
# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
