import sys
import copy
import math
from collections import deque
from prime import Prime
prime_man = Prime()

#obtain the name of the input
def fileName():
    filename = 'input'
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        print("File was not indicated")
        exit()
    return filename

fn = fileName()
file = open(fn, 'r')
out = open('output', 'w')

line_number = 1;
testcase = 1
max_testcases = 0
tc_ln = 0

while True:
    line = file.readline()
    if line:
        line = line.replace("\n","")
        inputs = line.split(" ")
        #how many test cases are
        if line_number == 1:
            max_testcases = int(inputs[0])
            line_number = 2
            tc_ln = 0
            continue

        N = int(inputs[0])
        J = int(inputs[1])

        numbers = []
        max_num = int(math.pow(2, N-2))
        add_num = int(math.pow(2, N-1)+1)
        for i in range(max_num):
            number = (2*i)+add_num
            bin_number = str(bin(number)).replace("0b","")
            number_data = {'bin': bin_number, 'div': []}

            is_prime = False
            for j in range(2,11):
                base = 1
                num_in_base = int(bin_number, j)
                divisor = prime_man.checkDivisor(num_in_base)

                if divisor > -1:
                    number_data['div'].append(divisor)
                else:
                    is_prime = True
                    break
            if not is_prime:
                numbers.append(number_data)
                if len(numbers) == J:
                    break

        out.write("Case #"+str(testcase)+":\n")
        for num in numbers:
            out.write(num['bin'])
            for divisor in num['div']:
                out.write(' ' + str(divisor))
            out.write("\n")
            out.flush()
        tc_ln = 0
        testcase = testcase + 1
        line_number += 1
    else:
        break
file.close()
out.close()
exit()