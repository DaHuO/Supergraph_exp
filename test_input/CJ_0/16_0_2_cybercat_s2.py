import sys

stack =[]

number = 0

def flip(idx, stack):

    global number
    number = number+1
    
    s_size = len(stack)

    
        
    

    for i in range(0, idx):
        
        if stack[i] == "-":
            stack[i] = "+"
        else:
            stack[i] = "-"

    return stack



def check(stack):
    if '-' in stack:
        return False
    else:
        return True


def go(cnt, stack):
    i = 0
    global number
    
    while True:

        if not "+" in stack:         
            print "Case #%d: %d"%(cnt, number + 1)
            number =0
            break
        
        if check(stack):
            print "Case #%d: %d"%(cnt, number)
            number =0
            break
            
        
        flag = False    
    
        for j in range(i+1, len(stack)):
            if stack[i] != stack[j]:
                flip(j, stack)
                flag = True
                break

        if flag:
            i = 0
        else:
            i= i+1
                
                       
        


input_lst = []
fd = open(sys.argv[1], 'r')
c=1
while True:
    line = fd.readline()
    if line =="":
        break
    
    if c ==1:
        num_input = int(line)
        
    else:
        
        input_lst.append(line)

    c = c+1
    

cnt =1


for in_stack in input_lst:
        
    for i in range(0, len(in_stack)):
        if "\n" != in_stack[i]:
            stack.append(in_stack[i])
            
    go(cnt, stack)
    #print stack
    stack=[]
    cnt = cnt +1


"""
in_stack = "+-"
for i in range(0, len(in_stack)):
        if "\n" != in_stack[i]:
            stack.append(in_stack[i])

go(1, stack)
"""














