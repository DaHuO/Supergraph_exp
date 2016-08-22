def remove_duplicates_and_count_minus(stack):
    new_stack = stack[0]
    minus = 0
    if stack[0] == '-':
        minus += 1
    for p in stack:
        if p != new_stack[-1]:
            if p == '-':
                minus += 1
            new_stack += p

    return minus

T = input()
for t in range(T):
    pancakes = raw_input()

    minus = remove_duplicates_and_count_minus(pancakes)

    if pancakes[0] == '-':
        ans = 2 * (minus - 1) + 1
    else:
        ans = 2 * minus

    print "Case #%d: %d" % ((t + 1), ans)

