def read_file(file):
    with open(file) as f:
        data = f.readlines()
        data = [x.strip('\n') for x in data]

    test_cases = int(data[0])
    sum_of_cases = []
    for test_cases in range(0,test_cases):
        sum_of_cases.append(data[test_cases + 1])

    return sum_of_cases


letter_list = ['ABCDEFGHIJKLMNOPQRSTUVWXYZ']

def check_value(letter, letter_list):
    for i in range(len(letter_list[0])):
        if letter_list[0][i] == letter:
            return i

def last_word(input):
    counter = 1
    to_return = ''
    return_list = []

    for i in range(len(input)):
        for x in range(len(input[i])):
            if to_return == '':
                to_return += input[i][x]
            else:
                value_1 = check_value(to_return[0], letter_list)
                value_2 = check_value(to_return[-1], letter_list)
                value_3 = check_value(input[i][x], letter_list)

                if value_1 > value_3 and value_1 > value_2:
                    temp = input[i][x]
                    new = ''.join((to_return, temp))
                    to_return = new
                elif value_3 == value_1:
                    temp = input[i][x]
                    new = ''.join((temp, to_return))
                    to_return = new
                elif value_3 == value_2:
                    temp = input[i][x]
                    new = ''.join((to_return, temp))
                    to_return = new
                elif value_3 > value_1:
                    temp = input[i][x]
                    new = ''.join((temp, to_return))
                    to_return = new
                elif value_1 == value_2:
                    temp = input[i][x]
                    new = ''.join((to_return, temp))
                    to_return = new
                else:
                    temp = input[i][x]
                    new = ''.join((temp, to_return))
                    to_return = new
        return_list.append('Case #' + str(counter) + ': ' + to_return)
        counter = counter + 1
        to_return = ''

    return return_list


god_cases = read_file('A-large.in')
def write_file(file, to_return):
    with open(file, 'r+') as f:
        for i in range(len(to_return)):
            if i != (len(to_return) - 1):
                f.write(to_return[i] + '\n')
            else:
                f.write(to_return[i])

    return file[0]

write_file('output.in', last_word(god_cases))