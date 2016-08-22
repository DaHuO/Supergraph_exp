for case in range(int(input())):
    stack = str(input())
    counter = 0
    if stack[-1] == '-':
        counter = 1

    for i in range(len(stack) - 1):
        if stack[i] != stack[i + 1]:
            counter += 1

    print('Case #' + str(case + 1) + ': ' + str(counter));