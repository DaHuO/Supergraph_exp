t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    curr_stack = input()

    started_happy = False
    happy = "+"
    flips = 0
    prev_pancake = "+"
    last_pancake = curr_stack[-1]
    toggled = False

    if curr_stack[0] == happy:
        started_happy = True

    for pancake in curr_stack:
        if pancake != prev_pancake:
            toggled = True
            flips += 1

        prev_pancake = pancake

    if toggled:
        if started_happy:
            flips += 1
        if last_pancake == happy:
            flips -= 1

    print("Case #{}: {}".format(i, flips))






