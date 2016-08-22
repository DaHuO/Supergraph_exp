from sys import stdin

lines = stdin.readlines()
t = 0
for stack in lines[1:]:
    t += 1
    last_pancake = ''
    if stack[0] == '-':
        flips = -1
    else:
        flips = 0
    for pancake in stack:
        if pancake == last_pancake:
            continue
        last_pancake = pancake
        if pancake == '-':
            flips += 2
    print "Case #%d: %d" % (t, flips)
        