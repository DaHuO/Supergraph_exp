import re


def flip_pancakes(stack, flip_index):
    stack = list(stack)
    if(flip_index >= len(stack)):
        return(-1)
    
    i = 0
    for i in range(flip_index + 1):
        if(stack[i] == '-'):
            stack[i] = '+'
        elif(stack[i] == '+'):
            stack[i] = '-'
        else:
            return(-1)
        
        i += 1
        
    return(''.join(stack))



def get_firstset_happy(stack):
    end_of_happy_index = 0
    
    for i,j in enumerate(stack):
        if(j == '+'):
            end_of_happy_index = i
        else:
            return(end_of_happy_index)



def get_last_sad(stack):
    pattern = re.compile('-')

    for m in pattern.finditer(stack):
        last_sad = m.start()
    return(last_sad)



g = open('D:\Users\john\My Documents\Google Code Jam\Google Code Jam 2016\pancake\pancake_sample_out.txt','w+')

with open('D:\Users\john\My Documents\Google Code Jam\Google Code Jam 2016\pancake\pancake_sample.txt', 'r+') as f:
    num_cases = int(f.readline())
    
    for i in range(num_cases):
        pan_stack = f.readline()
        flips = 0
        
        if('-' not in pan_stack):
            g.write('Case #' + str(i+1) + ': ' + str(0) + '\n')
        else:
            done = False
            
            while(not done):
                if('-' not in pan_stack):
                    done = True
                    break
                    
                if(pan_stack[0] == '-'):
                    last_sad_index = get_last_sad(pan_stack)
                    pan_stack = flip_pancakes(pan_stack, last_sad_index)
                    flips += 1
                else:
                    firstset_happy_index = get_firstset_happy(pan_stack)
                    pan_stack = flip_pancakes(pan_stack, firstset_happy_index)
                    flips += 1
            
            g.write('Case #' + str(i+1) + ': ' + str(flips) + '\n')
        
g.close()