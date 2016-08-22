import os

case_num = 1


def string_simplifier(string):
    final_string = ''
    for i in range(0,len(string)-1):
        if string[i] != string[i+1]:
            final_string = final_string + string[i]
    return final_string + string[len(string)-1]

def moves_needed(edited_string):
    length = len(edited_string)
    if edited_string[length - 1] == '+':
        return length - 1
    if edited_string[length - 1] == '-':
        return length

with open('B-large.in', 'rb') as text_file:
    t = text_file.readline().strip('\r\n')
    for line in text_file:
        line = line.strip('\r\n')
        print 'Case #%s: %s' % (case_num, moves_needed(string_simplifier(line)))
        case_num += 1

