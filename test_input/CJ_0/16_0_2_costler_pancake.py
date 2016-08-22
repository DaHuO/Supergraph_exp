from string import maketrans


stackflip = maketrans("+-","-+")
def flip(stack, i):
    return stack[:i].translate(stackflip) + stack[i:]


def flips(stack):
    if not '-' in stack:
        return 0

    i=1
    while i < len(stack):
        if stack[i] != stack[0]:
            break
        i+=1
    return 1 + flips(flip(stack, i))



T = int(raw_input())
for i in range(T):
    print "Case #%s: %s" % (i+1, flips(str(raw_input())))
