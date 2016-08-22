import math
# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
total = int(raw_input())  # read a line with a single integer
for i in xrange(1, total + 1):
    S = list(raw_input())
    output = []
    for x in S:
        if len(output) == 0:
            output.insert(0,x)
            continue
        if x < output[0]:
            output.append(x)
        else:
            output.insert(0,x)

    print "Case #{}: {}".format(i, "".join(output))
    # check out .format's specification for more formatting options
