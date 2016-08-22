

import os
import sys
OUTPUT_FILE_NAME = 'output_file.txt'
def Pancakes():
    input_file = open('input_file.txt', 'r')
    if(os.path.isfile(OUTPUT_FILE_NAME)):
        os.remove(OUTPUT_FILE_NAME)
    first = 0
    num_tests = 0
    test_number = 0
    for line in input_file:
        if(first == 0):
            num_tests = int(line)
            first = 1
        else:
            test_number = test_number + 1
            check_line(test_number, line.strip())
            if test_number == num_tests:
                print 'Done checking!!!'
                input_file.close()
                return 0
    return -1


def check_line(test_case_number, S):
    output_file = open(OUTPUT_FILE_NAME, 'a')

    length_of_pancakes = len(S)
    count = 0
    first = 0
    check = ''
    for idx in range(0,length_of_pancakes):
        if first == 0:
            check = S[idx]
            count = count + 1
            first = 1
        else:
            if check == '':
                print 'error!!!'
                sys.exit(-1)
            if S[idx] != check:
                count = count + 1
                check = S[idx]

    if S[-1] == '+':
        count = count - 1

    text = 'Case #' + str(test_case_number) + ': ' + str(count) + '\n'
    output_file.write(text)
    print text
    output_file.close()




if __name__ == "__main__":
    Pancakes()