import math
# File name
#input_file_name = "A-large-practice.in"
#input_file_name = "B-large.in"
input_file_name = "small.txt"
output_file_name = input_file_name + '.out'

# Input input_file
input_file = open(input_file_name, 'r')
output_file = open(output_file_name, 'w')

# Total cases
case_number = int(input_file.readline())

# Deal with each case
for case_i in range(case_number):

    # Always do some formating after split
    line = input_file.readline()
    N = int(line.split(' ')[0])
    J = int(line.split(' ')[1])

    # Initial the divider array
    div = []
    for i in range(2, 11):
        div.append([])

    # Find it
    num_i = 0
    ans_str = []
    while(1):
        # End condition
        if(len(ans_str) >= J):
            break

        # Generate binary string
        mid_str = str(bin(num_i))[2:]
        padding_str = '0' * (N - 2 - len(mid_str))
        binary_str = '1' + padding_str + mid_str + '1'

        # Convert to number and test
        binjo = True
        div_base = []
        for base in range(2, 11):
            number = int(binary_str, base)
            has_div = False
            max_div = int(math.sqrt(number)) + 1

            # Find divisor
            for j in range(2, max_div):
                if number % j == 0:
                    has_div = True
                    div_base.append(j)
                    break
            if has_div == False:
                binjo = False
        if binjo:
            ans_str.append(binary_str)
            for i in range(2, 11):
                div[i-2].append(div_base[i-2])
            print(len(ans_str))
        # Next iteration
        num_i = num_i + 1

    # Output to file
    output_file.write('Case #' + str(case_i + 1) + ':\n')
    for i in range(J):
        output_file.write(ans_str[i])
        for j in range(2, 11):
            output_file.write(' ' + str(div[j - 2][i]))
        output_file.write('\n')

input_file.close()
output_file.close()
