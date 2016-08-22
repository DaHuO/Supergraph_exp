import itertools, math, time

TIMEOUT = .1

print_result = True

def test_possible_jamcoin(jamstring):
    #start a timer - if this coin is taking too long to crack, try another
    startTime = time.clock()

    #iterate over every base interpretation of the jam coin
    divisors = [0] * 9
    for base in range(2,11):
        interpretation = int(jamstring, base)
        #try and find a divisor in that range
        for j in range(2, math.ceil(math.sqrt(interpretation))):
            if(time.clock() - startTime > TIMEOUT):
                return False

            if interpretation % j == 0:
                divisors[base-2] = j
                #print('base {} : {}/{}'.format(base, interpretation, j))
                break
        else:
            return False

    return divisors
# return a value corresponding to the output for case N. A newline will be appended automatically.
def do_problem(N, J):



    return 1

# this function is called once for each test case
def output_generator(input_file):
    #only ever one test case
    _ = int(f.readline())

    #read out N and J
    [N,J] = map(int, f.readline().split())

    middle_num_digits = N - 2                   #number of digits in the 'middle'
    max_middle = (1 << middle_num_digits) - 1   #max value of middle digits

    num_coins = 0

    #iterate over every possible jamcoin of length N
    for i in range(0, max_middle + 1):
        i_as_string= '1' + format(i,'b').zfill(middle_num_digits) + '1'
        result = test_possible_jamcoin(i_as_string)
        if result != False:
            result_string_line = str(i_as_string) + ' ' + ' '.join([ str(j) for j in result ]) + '\n'
            print(result_string_line)
            yield result_string_line
            num_coins += 1
            if num_coins == J:
                break

            #print(i_as_string, ": PASS")
        #else:
            #print(i_as_string, ": FAIL")
            #pass

    # result = do_problem(N,J)
    # result_string_line = 'Case #1:\n{}'.format(result)
    #
    # #optionally print result
    # if print_result:
    #     print(result_string_line, end='')



f = open('input.txt')
out_f = open('output.txt','w')

out_f.write('Case #1:\n')
out_f.writelines(output_generator(f))

