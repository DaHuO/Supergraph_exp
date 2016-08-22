import math, sys        

def load_info(f):
    line = f.readline()
    out = int(line)
    return out

def find_divisor(num):
    d = 0
    if num%2 == 0:
        d = 2
    else:
        root_of_n = num**(0.125)
        max_div = math.floor(root_of_n)
        for divisor in xrange(3, int(max_div+1), 2):
            if num%divisor == 0:
                d = divisor
                break
    return d    

def find_jamcoins(f, case_num):
    print_info = ['Case #' + str(case_num+1) + ': \n']
    line = f.readline()
    num_of_digits, num_of_jc = [int(y) for y in line.split(' ')]
    jc = 0
    initial_num = [x**(num_of_digits-1) + 1 for x in xrange(3,10)]
    initial_pow = []
    for base in xrange(3,10):
        temp = []
        power = num_of_digits-2
        while power > 0:
            temp.append(base**power)
            power -= 1
        initial_pow.append(temp)
    for x in xrange(2**(num_of_digits-1)+1, 2**num_of_digits-1, 2):
        binary_x = bin(x)[2:]
        d = [0 for y in xrange(9)]
        d[0] = find_divisor(x)
        d[8] = find_divisor(int(binary_x))
        if d[0] == 0 or d[8] == 0: continue
        i = 1
        for base in xrange(3,10):
            temp = initial_num[base-3]
            power = num_of_digits-2
            for digit in binary_x[1:-1]:
                temp +=  int(digit)*initial_pow[base-3][num_of_digits- 2 - power]
                power -= 1
            d[i] = find_divisor(temp)
            if d[i] > 0: i+=1
            else: break
        if i < 8: continue
        elif 0 not in d:
            print_info.append(binary_x + ' ')
            for divisor in d:
                print_info.append(str(divisor) + ' ')
            print_info.append('\n')
            jc += 1
            print(jc)
        if jc == num_of_jc:
            print(jc)
            break
    return print_info

if __name__ == '__main__':
    while True:
        print('\n---------------------------')
        print("Type in the input and output files' names separated by a white space, or 'exit' when you're done, thx. ")
        
        sys.stdout.write('Coin Jam > ')
        input_args = str(raw_input())
        try:
            if input_args == 'exit':
                break
            elif input_args == '':
                continue
            else:
                args = input_args.split(' ')
                input_file = args[0]
                output_file = args[1]
        except:
            print('Invalid input. Please try again.')
        else:
            f_in = open(input_file)
            f_out = open(output_file, 'w')
            
            num_of_tests = load_info(f_in)
            try:
                for x in xrange(num_of_tests):
                    f_out.writelines(find_jamcoins(f_in, x))
            except:
                print('something wrong')
            else:
                print('File is built successfully!!!!')
                print('---------------------------\n')
            finally: 
                f_in.close()
                f_out.close()
        
        
