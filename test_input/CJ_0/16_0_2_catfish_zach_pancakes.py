import sys

def main():

    r_file = open('B-large.in','r')
    w_file = open('pancake_output.txt','w')

    t = int(r_file.readline())

    for x in range(t):

        outputString = 'Case #{}: {}\n'.format(x + 1, pancake1(r_file.readline()[:-1]))

        w_file.write(outputString)

    r_file.close(); w_file.close();

''' doesn't work.
def pancake(string):
    n = 0
    stack = convertToBools(string)
    x = len(stack) - 1
    while True:

        assert x > -1, 'x out of range.'
        
        if stack[0] == False and False not in stack[1:]: return n + 1
        if False not in stack: return n
        currentElement = stack[x]
        
        if currentElement == True:
            x -= 1
            continue

        else: # the bottom element needs to be made true,

            if stack[0] == True: # pancake needs to be flipped at the top:
                stack[0] = False
                n += 1

            if False not in stack: return n
            if True not in stack: return n + 1
            # flip the stack from the bottom
            toFlip = stack[:x + 1]

            toFlip = [not v for v in toFlip][::-1] # reverse list and invert it
            n += 1
            stack = toFlip + stack[x + 1:]

            if False not in stack: return n





        x -= 1      
'''
def pancake1(string):
    n = 0
    stack = convertToBools(string)

    
    i = 0
    while True:

        if False not in stack: return n
        if True not in stack: return n + 1
        first = stack[i]
        
        for element in stack:
            if stack[i] != first: #there is a difference
                stack[:i] = [not v for v in stack[:i]]
                n += 1
                break
            i += 1 

def convertToBools(string):

    boolList = []

    for character in string:
        if character == '+':
            boolList.append(True)

        elif character == '-':
            boolList.append(False)

    return boolList

if __name__ == '__main__':
    main()
