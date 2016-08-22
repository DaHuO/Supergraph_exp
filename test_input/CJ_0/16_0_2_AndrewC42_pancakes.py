cases = int(raw_input())
for i in range(1, cases + 1):
    stack = raw_input()
    flips = 0


    # rather than actually changing all the values, change the meaning of the
    # 'happy side' whenever the stack is flipped
    happy_side = '+'

    for j in range(1, len(stack)+1):
        pancake = stack[len(stack)-j]

        #skip if the current pancake is happy
        if pancake == happy_side:
            continue

        # flip stack and continue
        flips += 1

        if happy_side == '+':
            happy_side = '-'
        else:
            happy_side = '+'

    print "Case #{}: {}".format(i, flips)
