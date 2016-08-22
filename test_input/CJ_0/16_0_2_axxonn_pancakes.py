t = int(raw_input())
for case in range(1, t+1):
    stack = raw_input()
    count = 0
    cur = ''
    for pancake in stack:
        if pancake != cur:
            count += 1
            cur = pancake
    if stack[-1] == '+':
        count -= 1
    print "Case #%d: %d" % (case, count)
