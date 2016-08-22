from collections import deque
from sets import Set

input = open('./B.in', 'r').readlines()
output = open('./B.out', 'w')

inputQueue = deque(input)
testCases = int(inputQueue.popleft())
for i in range(1, testCases+1):
    stack = str(inputQueue.popleft()).rstrip().rstrip("+")

    count = 0
    if len(stack) > 0:
        state = stack[0]

        print stack
        for pancake in stack:
            if pancake == state:
                continue
            else:
                state = pancake
                count += 1
        outputString = str(count + 1)
    else:
        outputString = str(0)
    print outputString
    output.write("Case #"+str(i)+": "+outputString+"\n")
output.close()