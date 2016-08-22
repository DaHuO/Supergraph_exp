import sys
import math
from itertools import product

def convert_to_base(coin_jam,base):
    """
    """
    suma = 0
    index = 1
    for bit in reversed(coin_jam):
        if int(bit):
            suma += index
        index *= base
    return suma

def is_prime(number):
    """
    """
    if number >= 0 and number < 2:
        return False,False
    if number == 2 :
        return True,False

    if number % 2 == 0 :
        return False,2

    sqr = int(math.sqrt(number)) + 1

    for divisor in xrange(3,sqr,2):
        if number % divisor == 0:
            return False,divisor
    else:
        return True,False

def produce_jam_coins(line_list):
    length = int(line_list[0])
    max_result = int(line_list[1])
    line_printed = 0
    for combination in product('01',repeat=length):
        nontrivial_string = ''
        if combination[0] == '1' and combination[-1] == '1':
            for base in xrange(2,11):
                number = convert_to_base(combination,base)
                is_prime_nontirivial = is_prime(number)
                if is_prime_nontirivial[0]:
                    break
                
                if is_prime_nontirivial[1] == number:
                    print 'aaaa'
                    
                nontrivial_string += ' {}'.format(is_prime_nontirivial[1])
            else:
                print '{} {}'.format(''.join(combination),nontrivial_string)
                line_printed += 1
                if line_printed == max_result:
                    break
        else:
            continue    
       



try:
    file_name = sys.argv[1]
except:
    print 5 * 'TEST '
    file_name = 'test.in'

with open(file_name,'r') as input_obj:
    input_obj.next()
    for test,line in enumerate(input_obj,1):
        line_list = line.split()
        print 'Case #{}:'.format(test)
        produce_jam_coins(line_list)
        

