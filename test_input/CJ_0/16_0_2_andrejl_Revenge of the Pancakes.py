for iteration in range(1, int(input()) + 1):
    stack = list(input().strip()[:])

    operations = 0
    i = 0
    while i < len(stack):
        was_inside = False
        while i < len(stack) and stack[i] == '+':
            was_inside = True
            i += 1
        if i == len(stack):
            break
        if was_inside:
            operations += 1

        while i < len(stack) and stack[i] == '-':
            i += 1
        operations += 1


    print("Case #{0}: {1}".format(iteration, operations))
