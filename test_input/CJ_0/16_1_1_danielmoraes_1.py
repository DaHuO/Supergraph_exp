t = int(raw_input())

for i in xrange(1, t + 1):
    l = []

    s = raw_input()
    l.append(s[0])

    for letter in s[1:]:
        if letter >= l[0]:
            l = [letter] + l
        else:
            l.append(letter)

    print "Case #{}: {}".format(i, "".join(l))
