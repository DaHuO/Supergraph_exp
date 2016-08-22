
import sys
import string

fname = sys.argv[1]

def isEmpty(stack):
    return stack == []

def notEmpty(stack):
    return stack != []

def push(stack, item):
    stack.append(item)

def pop(stack):
    return stack.pop()

def flip(p):
    if p == '-':
        return '+'
    else:
        return '-'

def happy(stack):
    '''check if all pancakes on the stack are happy'''

    for p in stack:
        if p == '-':
            return False

    return True

with open(fname) as f:
    # T - number of test cases
    T = int(string.split(f.readline())[0])
    #print "T {}".format(T)

    for t in range(T):
        # stack string
        s = f.readline()[:-1]

        # for each pancake push it on the stack
        stack = []
        for p in s:
            push(stack, p)
        stack.reverse()
        #print "{}".format(stack)

        i = 0
        # flip the top of the stack (same side up)
        while not happy(stack):
            first = pop(stack)
            fstack = []
            push(fstack, flip(first))
            while notEmpty(stack):
                next = pop(stack)
                if first == next:
                    push(fstack, flip(next))
                else:
                    push(stack, next)
                    break

            # Now push them back on the stack
            while notEmpty(fstack):
                push(stack, pop(fstack))
            #print "i {}: {}".format(i, stack)

            i += 1

        print("Case #{}: {}".format(t+1, i))
                


