from sys import argv
import copy

script, in_file, out_file = argv
input = open(in_file)
content = input.read().splitlines()
input.close()

test_count = 0
test_cases = []
line_index = 0
results = []

for line in content:
    if(line_index == 0):
        test_count = int(line)
    else:
        test_cases.append(line)
        
    line_index += 1
    

for case in test_cases:
    stack = list(case)
    l = len(stack)
    idx_end = -1
    idx_start = 0
    count_flip = 0
    finish = False
    negative_found = False
    while(finish == False):
        for idx_end in range(-1, (-l - 1), -1):
            if(stack[idx_end] == '-'):
                negative_found = True
                break
        if(negative_found == False):
            break
            
        if(stack[0] == '+'):
            for idx_start in range(0, (l)):
                if(stack[idx_start] == '-'):
                    for i in range(0,idx_start):
                        stack [i] = '-'
                    count_flip += 1
                    break          
        for i in range(0,(l + 1 + idx_end)):
            if(stack[i] == '-'):
                stack[i] = '+'
            else:
                stack[i] = '-'
            if(i == 0):
                count_flip += 1
        a = copy.copy(stack[:(l + 1 + idx_end)])
        a.reverse()
        a = a + stack[l + idx_end + 1:]
        
        stack = copy.copy(a)
        finish = True
        for i in range(0, l):
            if(stack[i] == '-'):
                finish = False
                break
    results.append(count_flip)

output = open(out_file, "wb")
for res_idx in range(1,(test_count + 1)):
    output.write("Case #" + str(res_idx) + ": " + str(results[res_idx - 1]) + "\n")
output.close()   
    
    
                