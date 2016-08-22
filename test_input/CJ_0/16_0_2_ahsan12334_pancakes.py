# Google Code Jam 2016
# Qualification Round
# Revenge of the Pancakes

def find_index(s):
    can1 = s.find('+-')
    can2 = s.find('-+')

    if can1 == -1 and can2 != -1:
        return can2
    elif can2 == -1 and can1 != -1:
        return can1
    elif can2 == -1 and can2 == -1:
        return len(s)-1
    else:
        return min(can1, can2)

def flip_string(index, s):
    iter = 0
    new_s = ''
    while(iter <= index):
        if s[iter] == '-':
            new_s = new_s + '+'
        else:
            new_s = new_s + '-'

        iter += 1
    # Reverse the string
    new_s = new_s[::-1]
    # Insert the rest of the string
    iter = index + 1
    while(iter < len(s)):
        new_s = new_s + s[iter]
        iter += 1
    return new_s

if __name__ == "__main__":
    input_file = open('B-large.in', 'r')
    test_cases = [x for x in input_file.read().split('\n')[1:] if x != ""]
    input_file.close()

    number_of_flips = []
    for s in test_cases:
        if '-' not in s:
            number_of_flips.append(0)
        else:
            flips = 0
            while('-' in s):
                flips += 1
                index = find_index(s)
                s = flip_string(index, s)
            number_of_flips.append(flips)

    with open('output.txt', 'w') as f:
        case_number = 1
        for n in number_of_flips:
            f.write('Case #{0}: {1}\n'.format(case_number, n))
            case_number += 1