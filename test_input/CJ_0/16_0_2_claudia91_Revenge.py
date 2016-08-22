'''
Created on 09 apr 2016

@author: claudia91
'''
from common import test_case


def solve_problem(test_case):
    move = 0
    if test_case[-1] == '-':
        move += 1
    
    
    for index in range(0,len(test_case)-1):
        if test_case[index] != test_case[index + 1]:
            move += 1
        else:
            move += 0
    return move

def solve(data):
    return solve_problem(data[0].strip(' \t\n\r'))
#open Output file
output = open(test_case.OUTPUT_FILE, 'w')
#read lines from input file
lines = test_case.read_file(test_case.INPUT_FILE)
for line in range(1, len(lines)):
    test_case.print_result(line, solve([lines[line]]), output)

# print solve_problem('--+-')
# print solve_problem('-')
# print solve_problem('-+')
# print solve_problem('+-')
#print solve_problem('+++')
# print solve_problem('++--++-++')





