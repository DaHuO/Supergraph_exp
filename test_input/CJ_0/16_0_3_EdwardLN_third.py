from __future__ import print_function
import random

def is_prime(n):
    return all([(n%j) for j in range(2, int(n**0.5)+1)]) and n>1

def divisorFun(n):
    for i in xrange(2,n/2+1):
        if n%i == 0:
            return i

def coin_jam(input_file, output_file):
    with open(input_file) as input_f:
        with open(output_file, 'w') as output_f:
            print('Case #1:', file=output_f)
            n = input_f.readline().strip()
            length, num = input_f.read().split(' ')
            start = ''.join(['1', '0'*(int(length)-2), '1'])
            end = '1'*int(length)
            mas_of_posible_jams = list()
            count = 0
            used = set()
            for elem in range(int(start,2), int(end,2)+1):
                format_elem = format(elem, 'b')
                if format_elem.endswith('1'):
                    mas_of_posible_jams.append(format_elem)
            while (count < int(num)):
                result_mas = []
                rand_jam = random.sample(mas_of_posible_jams, 1)[0]
                mas_of_posible_jams.remove(rand_jam)
                rand_jam_mas = [rand_jam]
                check_mas = [is_prime(int(rand_jam, i)) for i in range(2,11)]
                if True not in check_mas:
                    int_check_mas = [int(rand_jam, i) for i in range(2,11)]
                    for elem in int_check_mas:
                        divisor = divisorFun(elem)
                        result_mas.append(divisor)
                    rand_jam_mas.extend(result_mas)
                    print(' '.join([str(elem) for elem in rand_jam_mas]),
                          file=output_f)
                    count += 1
                else:
                    pass
                    
                    
                    
                
            
            
            
        
            
            
