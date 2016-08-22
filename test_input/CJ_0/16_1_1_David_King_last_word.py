import sys

def load_info(f):
    line = f.readline()
    out = int(line)
    return out

def last_word(f, case_num):
    print_info = []
    line = f.readline()
    org_word = list(line.strip('\n'))
    last_word = []
    max_l = 'A'
    for letter in org_word:
        if letter >= max_l:
            last_word.insert(0, letter)
            max_l = letter
        else:
            last_word.append(letter)
    
    print_info.append('Case #' + str(case_num+1) + ': ')
    for letter in last_word:
        print_info.append(str(letter))
    print_info.append('\n')

    
    return print_info

if __name__ == '__main__':
    while True:
        print('\n---------------------------')
        print("Type in the input and output files' names separated by a white space, or 'exit' when you're done, thx. ")
        
        sys.stdout.write('The Last Word > ')
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
                    f_out.writelines(last_word(f_in, x))
            except:
                print('something wrong')
            else:
                print('File is built successfully!!!!')
                print('---------------------------\n')
            finally: 
                f_in.close()
                f_out.close()
        
