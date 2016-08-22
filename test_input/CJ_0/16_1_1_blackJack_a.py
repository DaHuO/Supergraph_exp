i = int(raw_input())

for curr in range(i):
    string = raw_input()
    new = ''
    for c in string:
        if not new:
            new = c
        elif new[0] > c:
            new = new + c
        else:
            new = c + new
    print "Case #{0}: {1}".format(curr+1, new)
