

import os
import sys
from random import randint
OUTPUT_FILE_NAME = 'output_file.txt'
def Coin_Jam():
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
            check_line(test_number, line)
            if test_number == num_tests:
                print 'Done checking!!!'
                input_file.close()
                return 0
    print 'This should not happen'
    return -1


def check_line(test_case_number, line):
    output_file = open(OUTPUT_FILE_NAME, 'a')
    output_file.write('Case #' + str(test_case_number) + ':\n')
    arg_list = line.split()
    N = int(arg_list[0])
    J = int(arg_list[1])
    num_placeholders = 2

    chosen_jam_coin = []
    failed_jam_coin = []
    example = 0
    while example != int(J):
        base_list = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        reverse_order_possible_jam_coin = '1'
        for idx in range(0, N-num_placeholders):
            reverse_order_possible_jam_coin = reverse_order_possible_jam_coin + str(randint(0,1))

        reverse_order_possible_jam_coin = reverse_order_possible_jam_coin + '1'
        if reverse_order_possible_jam_coin in failed_jam_coin or reverse_order_possible_jam_coin in chosen_jam_coin:
            continue


        count = 0
        for idx in range(0, len(reverse_order_possible_jam_coin)):
            count = count + int(reverse_order_possible_jam_coin[idx])

        for idx in range(0, N):
            base_list[0] = base_list[0] + int(reverse_order_possible_jam_coin[idx]) * pow(2, idx)
            base_list[1] = base_list[1] + int(reverse_order_possible_jam_coin[idx]) * pow(3, idx)
            base_list[2] = base_list[2] + int(reverse_order_possible_jam_coin[idx]) * pow(4, idx)
            base_list[3] = base_list[3] + int(reverse_order_possible_jam_coin[idx]) * pow(5, idx)
            base_list[4] = base_list[4] + int(reverse_order_possible_jam_coin[idx]) * pow(6, idx)
            base_list[5] = base_list[5] + int(reverse_order_possible_jam_coin[idx]) * pow(7, idx)
            base_list[6] = base_list[6] + int(reverse_order_possible_jam_coin[idx]) * pow(8, idx)
            base_list[7] = base_list[7] + int(reverse_order_possible_jam_coin[idx]) * pow(9, idx)

        base_list[8] = int(reverse_order_possible_jam_coin[::-1])
        divisor_list = []

        print 'Testing for jam coin base 10 value: ' + str(base_list[8])
        for idx, base in enumerate(base_list):
            divisor = 2
            divisor_found = False
            while divisor < base and divisor <= 103 and not divisor_found:
                (q, r) = divmod(base, divisor)
                if r != 0:
                    divisor = divisor + 1
                    continue
                divisor_list.append(divisor)
                print 'Found divisor for base ' + str(idx+2) + ' value ' + str(base) + '\n'
                divisor_found = True

            if not divisor_found:
                print 'Error. Did not find divisor for base' + str(idx+2) + ' value ' + str(base) + '\n'
                print 'Restarting find'
                failed_jam_coin.append(reverse_order_possible_jam_coin)
                break
        if not divisor_found:
            continue
        if len(divisor_list) == 9:
            chosen_jam_coin.append(reverse_order_possible_jam_coin)
            example = example + 1

            left_to_right_order_jam_coin = reverse_order_possible_jam_coin[::-1]
            print 'jam_coin: ' + left_to_right_order_jam_coin
            output_file.write(left_to_right_order_jam_coin)
            for idx,divisor in enumerate(divisor_list):
                output_file.write(' ' + str(divisor))
                print 'Base: ' + str(base_list[idx])
                print 'Divisor: ' + str(divisor)
            output_file.write('\n')



    output_file.close()




if __name__ == "__main__":
    Coin_Jam()