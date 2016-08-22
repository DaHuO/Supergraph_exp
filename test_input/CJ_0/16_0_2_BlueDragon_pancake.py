

'''
Have a stack of booleans. Need to make all of them true,
only using the flip operation.
'''


def flip(stack, count):
    temp = stack[-count:]
    temp.reverse()
    stack[-count:] = temp
    for index in range(len(stack) - count, len(stack)):
        if stack[index] == '+':
            stack[index] = '-'
        else:
            stack[index] = '+'
    return stack


def pancake():
    file = open("/home/aidan/Documents/codejam16/B-large.in")
    outFile = open("/home/aidan/Documents/codejam16/pancake-large.out", "w")
    file.readline()  # Discard number of tests

    for index, line in enumerate(file):
        stack = list(line.strip())  # Delicious pancakes
        stack.reverse()  # Top of the stack is on the right
        stack = "".join(stack)
        flips = 0
        while '-' in stack:  # While pancakes are still sad
            if stack[-1] == '+':
                rindex = stack.rfind('-')
            else:
                rindex = stack.rfind('+')
            stack = ''.join(flip(list(stack), len(stack) - 1 - rindex))
            flips += 1
        outFile.write("Case #{}: {}\n".format(index+1, flips))

if __name__ == "__main__":
    pancake()


