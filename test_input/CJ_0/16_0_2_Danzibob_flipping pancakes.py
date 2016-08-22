def read(file):
    with open(file,'r') as f:
        inp = [line[:-1] if '\n' in line else line for line in f]
    for line in inp:
        yield line
def add_line(file,line):
    with open(file,'a') as f:
        f.write(line+"\n")
def flip(stack,num):
    for i in range(num+1):
        stack[i] = not stack[i]
    return stack
def find_last(stack):
    bstack = stack[::-1]
    pos = len(stack)-1-bstack.index(False)
    return pos
f = read('input.txt')
num_lines = int(next(f))
cn = 1
for stack in f:
    case_text = "Case #{}: ".format(cn)
    stack = [p=='+' for p in stack]
    counter = 0
    while False in stack:
        stack = flip(stack,find_last(stack))
        counter += 1
    add_line('output.txt',(case_text+str(counter)))
    cn += 1
    
        
