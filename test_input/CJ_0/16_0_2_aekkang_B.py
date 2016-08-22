# Flip the stack at the flip_at index (inclusive).
def flip(stack, flip_at):
    stack[0:flip_at] = ["+" if j == "-" else "-" for j in stack[flip_at-1::-1]]

# Number of test cases.
T = input()

for i in range(T):
    stack = list(raw_input())
    flips = 0

    # The algorithm below depends on the fact that we want all blank side up
    # pancakes at the top to be flipped while also bringing blank side up
    # pancakes near the bottom to come up to the top.

    # While not all pancakes are happy side up:
    while stack != ["+"] * len(stack):
        # If the top pancake is happy side up, then flip all consecutive happy
        # side up pancakes at the top. Else, find the bottom-most blank side
        # up pancake and flip at that pancake.
        if stack[0] == "+":
            flip_at = stack.index("-")
        else:
            flip_at = len(stack) - stack[::-1].index("-")

        flip(stack, flip_at)
        flips += 1

    print "Case #%d: %d" % (i + 1, flips)