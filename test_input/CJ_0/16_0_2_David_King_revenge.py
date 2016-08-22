import sys

def load_info(f):
    line = f.readline()
    out = int(line)
    return out

def flip_pancakes(f, case_num):
    print_info = []
    line = f.readline()
    pancakes = str(line)    
    flip_times = 0
    if '-' not in pancakes: pass
    else:        
        i = 0
        for cake in pancakes:
            if i == 0:
                if cake == '-':
                    last_cake = '-'
                    flip_times += 1
                else:
                    last_cake = '+'
            else:
                if cake == last_cake: pass
                elif cake == '-':
                    last_cake = '-'
                    flip_times += 2
                else:
                    last_cake = '+'
            i += 1
    
    
    print_info.append('Case #' + str(case_num+1) + ': ' + str(flip_times))
    print_info.append('\n')

    
    return print_info

if __name__ == '__main__':
    while True:
        print('\n---------------------------')
        print("Type in the input and output files' names separated by a white space, or 'exit' when you're done, thx. ")
        
        sys.stdout.write('Flip pancakes> ')
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
                    f_out.writelines(flip_pancakes(f_in, x))
            except:
                print('something wrong')
            else:
                print('File is built successfully!!!!')
                print('---------------------------\n')
            finally: 
                f_in.close()
                f_out.close()
        
