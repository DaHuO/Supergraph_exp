def flip(stack, i):
    #print("fllipping at {}".format(i))
    mini = stack[:i]
    mini.reverse()
    revMini = [not x for x in mini]

    stack = revMini + stack[i:]
    return stack

def flipUntilHappy(pancakes, case):
    finalStep = 0

    for j in range(0, 2):
        find = bool(j)
        step = 0
        stack = pancakes.copy()

        while(sum(stack) != len(stack)):
            if(sum(stack) == 0):
                stack = flip(stack, len(stack))
            else:
                i = stack.index(find)
                stack = flip(stack, i)
                find = not find
            step+=1

        if(finalStep == 0 or step < finalStep):
            finalStep = step

    print("Case #{}: {}".format(case+1, finalStep))

def generateStack(inputStr):
    l = []
    for char in inputStr:
        if(char=="+"):
            l.append(True)
        else:
            l.append(False)
    return l

def main():
    tests = int(input(""))

    for i in range(0, tests):
        stack = generateStack(input())
        flipUntilHappy(stack, i)

main()
