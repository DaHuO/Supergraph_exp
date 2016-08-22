case_count = int(raw_input())
for case_number in xrange(1, case_count + 1):
    full_stack = raw_input()
    collapsed_stack = [full_stack[0]]
    for pancake in full_stack[1:]:
        if pancake != collapsed_stack[-1]:
            collapsed_stack.append(pancake)

    last_blank = collapsed_stack[-1] == "-"
    flips = len(collapsed_stack) if last_blank else len(collapsed_stack) - 1

    print "Case #{}: {}".format(case_number, flips)
