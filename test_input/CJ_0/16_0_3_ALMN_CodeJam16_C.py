import os
import math
#from datetime import datetime
#start_time = datetime.now()

case_num = 1

#Takes the number in the specified base and converts it to base 10.
def convert_to_base10(number, base):
    num_str = str(number)
    num_base10 = 0
    for i in range(0,len(num_str)):
        num_base10 += int(num_str[i]) * base ** (len(num_str) - i - 1)
    return num_base10

#Takes the base 10 number and converts it to binary.
def base10_to_bin(x):
    bin_num = ''
    while x > 1:
        if x % 2 == 0:
            bin_num = bin_num + '0'
        else:
            bin_num = bin_num + '1'
        x = math.floor(x / 2)
    bin_num = bin_num + '1'
    bin_num = bin_num[::-1]
    return int(bin_num)

#this function returns 0 if the input is prime, and the first nontrivial divisor if it isn't.
def divisor_or_prime(x):
    if x == 2 or x == 3:
        return 0
    elif x / int(math.ceil(math.sqrt(x))) == math.sqrt(x):
        return math.sqrt(x)
    else:
        for n in range(2, int(math.ceil(math.sqrt(x)))):
            if x % n == 0:
                return n
                break
        else:
            return 0

with open('C-small-attempt0.in', 'rb') as text_file:
    t = text_file.readline().strip('\r\n')
    for line in text_file:
        line = line.strip('\r\n').split()
        N = int(line[0])
        J = int(line[1])
        jamcoins_found = 0
        #The jamcoins start with 2^(N-1), but have to add 1 since jamcoins only end in 1.
        test_n = 2**(N-1) + 1
        print 'Case #%s:' % (case_num)
        while jamcoins_found < J:
            pairs = []
            jamtest = base10_to_bin(test_n)
            for i in range(2, 11):
                b10_num = convert_to_base10(jamtest, i)
                if divisor_or_prime(b10_num) == 0:
                    break
                else:
                    pairs.append(int(divisor_or_prime(b10_num)))
            if len(pairs) == 9:
                string_answer = str(jamtest)
                for k in range(0, 9):
                    string_answer = string_answer + " " + str(pairs[k])
                print string_answer
                jamcoins_found += 1
            #add 2 to the test value since jamcoins only end in 1.
            test_n += 2
        case_num += 1

#print datetime.now() - start_time
