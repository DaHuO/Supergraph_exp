
# 5
# -       Case #1: 1
# -+      Case #2: 1
# +-      Case #3: 2
# +++     Case #4: 0
# --+-    Case #5: 3


def count_changes(pancake_stack):
    count = 0
    for i, char in enumerate(pancake_stack):
        if len(pancake_stack) > i+1 and pancake_stack[i+1] != char:
            count += 1

    if pancake_stack[len(pancake_stack)-1] == "-":
        count += 1

    return count


file_name = "B-large.in"

with open(file_name, "r") as f:
    lines = f.readlines()

    for i, pancake_stack in enumerate(lines[1:]):
        print("Case #{}: {}".format(i+1, count_changes(pancake_stack.strip())))
