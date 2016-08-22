cases = input()


def successor(stack, move):
    move += 1
    new_stack = [""] * len(stack)
    for i in xrange(len(stack)):
        if i < move:
            new_stack[i] = "+" if stack[move - 1 - i] is "-" else "-"
        else:
            new_stack[i] = stack[i]
    return "".join(new_stack)

for T in xrange(cases):
    pancakes = raw_input().strip()
    num = len(pancakes)

    count = 0
    index = num - 1

    while index >= 0:
        if pancakes[index] is "+":
            index -= 1
            continue

        if pancakes[0] is "-":
            flip = index
            index -= 1
        else:
            flip = index
            while pancakes[flip] is "-":
                flip -= 1

        pancakes = successor(pancakes, flip)
        count += 1

    print "Case #%d: %d" % (T + 1, count)
