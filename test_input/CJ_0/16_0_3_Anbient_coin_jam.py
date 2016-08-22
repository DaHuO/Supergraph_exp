from __future__ import print_function

import math

def is_prime(n):
    if n % 2 == 0 and n > 2:
        return 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return i
    return

def gen_padded_str(number, length):
    result = "{0:b}".format(number)
    result = '1' + ((length-2) - len(result)) * '0' + result + '1'
    return result



def coin_jam_generator(N, J):
    isValid = True

    count = 0
    str_constr = 0

    result = [[0 for x in range(10)] for x in range(J)]


    start_str = '1' + (N-2) * '0' + '1'

    #print("start string: %s" % start_str)

    while(count < J):
        result[count][0] = start_str
        for baseNr in xrange(2, 11):
            temp = int(start_str, baseNr)
            #print("%d\n" % temp)
            divisor = is_prime(temp)
            if (divisor is None):
                str_constr += 1
                start_str = gen_padded_str(str_constr, N)
                #print("start string: %s" % start_str)
                isValid = False
                break
            else:
                result[count][baseNr-1] = int(divisor)
        if (isValid == False):
            isValid = True
        else:
            count += 1
            str_constr += 1
            start_str = gen_padded_str(str_constr, N)
            #print("start string: %s" % start_str)

    return result

if __name__ == "__main__":
    testcases = input()
    for caseNr in xrange(1, testcases+1):
        N, J = raw_input().split(" ")
        result = coin_jam_generator(int(N), int(J))
        print("Case #%i:\n" % (caseNr))
        #print result
        for resNr in xrange(0, int(J)):
            for index in xrange(0, 10):
                print("%s " % str(result[resNr][index]), end="")
            print("\n")