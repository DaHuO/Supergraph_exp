def read_int():
    return int(raw_input())


def get_pancakes_array():
    return map(str, raw_input())


def flip_pancakes(stack, last_index_included):
    """Flip items from index 0 to last_index_included both included"""
    new_stack = []

    # Flip order of pancackes
    new_stack[0:last_index_included+1] = stack[last_index_included::-1]

    # Reverse values of flipped pancackes
    for i in range(0, len(new_stack)):
        if new_stack[i] == '-':
            new_stack[i] = '+'
        else:
            new_stack[i] = '-'

    # Copy same values to new stack
    new_stack.extend(stack[last_index_included+1:])

    return new_stack


_T = read_int()  # nbr of test cases
for _t in range(_T):
    tower = get_pancakes_array()
    # print("Initial tower: %s" % tower)
    total_iterations = 0

    for i in range(0, len(tower)-1):
        if tower[i] != tower[i+1]:
            # print("Need to flip from top to index %d for tower %s" % (i, tower))
            tower = flip_pancakes(tower, i)
            # print("Result: %s" % tower)
            total_iterations+=1

    # At that point, all the items are equal, either all '-' or all '+'
    # print("Uniform tower: %s" % tower)
    if tower[0] == '-':
        tower = flip_pancakes(tower, len(tower)-1) # we want all '+'
        total_iterations+=1

    # print("Result tower: %s" % tower)
    print("Case #%d: %s" % (_t+1, total_iterations))

    # print("\n\n")
