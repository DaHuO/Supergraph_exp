with open("t2.in") as f:
    content = f.readlines()


case = 0

for stack in content[1:]:
    case += 1

    numOfFlips = 0
    for i in range ( len(stack)-1, -1, -1):
        # i is position
        if stack[i] == "-" and (numOfFlips % 2 == 0):
            numOfFlips += 1

        elif stack[i] == "+" and (numOfFlips % 2 == 1):
            numOfFlips += 1

    print("Case #"+str(case)+": " + str(numOfFlips))


