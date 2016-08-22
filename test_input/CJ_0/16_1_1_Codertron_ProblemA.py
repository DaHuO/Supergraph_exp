

import os

OUTPUT_FILE_NAME = 'output_file.txt'
def ProblemA():
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
            check_number(test_number, line.strip())
            if test_number == num_tests:
                print 'Done checking!!!'
                input_file.close()
                return 0
    print 'This should not happen'
    return -1


def check_number(test_case_number, S):
    output_file = open(OUTPUT_FILE_NAME, 'a')
    first = True
    text = ''
    for idx in range(0,len(S)):
        if first:
            first = False
            text = S[idx]
        elif ord(S[idx]) == ord(text[0]) or ord(S[idx]) > ord(text[0]):
            text = S[idx] + text
        else:
            text = text + S[idx]
    print S
    print text
    output_file.write('Case #' + str(test_case_number) + ': ' + text + '\n')

    output_file.close()



if __name__ == "__main__":
    ProblemA()