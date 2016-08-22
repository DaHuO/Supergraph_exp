import csv, sys, random, math


def solve(cur_case, input_line):
    input_len = len(input_line.rstrip('\n'))
    count = 0
    
    for i in xrange(input_len - 1):
        if input_line[i] != input_line[i + 1]:
            count += 1
    if input_line[input_len - 1] == '-':
        count += 1
    return count
    

target = open("prob2_output_large.txt", 'w')
with open('large2.txt','r') as f:
    T = int(f.readline())    
    for i in xrange(T):
        input_line = str(f.readline())
        case_num = str(i+1)
        sol_str = 'Case #' + case_num +  ': ' + str( solve(i + 1,input_line)  ) + '\n'
        target.write( str(sol_str) )
        
    






