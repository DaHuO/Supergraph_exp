import os

case_num = 1
let_to_num = {
    'A' : 1,
    'B' : 2,
    'C' : 3,
    'D' : 4,
    'E' : 5,
    'F' : 6,
    'G' : 7,
    'H' : 8,
    'I' : 9,
    'J' : 10,
    'K' : 11,
    'L' : 12,
    'M' : 13,
    'N' : 14,
    'O' : 15,
    'P' : 16,
    'Q' : 17,
    'R' : 18,
    'S' : 19,
    'T' : 20,
    'U' : 21,
    'V' : 22,
    'W' : 23,
    'X' : 24,
    'Y' : 25,
    'Z' : 26
    }

def string_simplifier(string):
    final_string = string[0]
    for i in range(1,len(string)):
        if let_to_num[string[i]] < let_to_num[final_string[0]]:
            final_string = final_string + string[i]
        else:
            final_string = string[i] + final_string
    return final_string
        


with open('A-large.in', 'rb') as text_file:
    t = text_file.readline().strip('\r\n')
    for line in text_file:
        line = line.strip('\r\n')
        print 'Case #%s: %s' % (case_num, string_simplifier(line))
        case_num += 1


