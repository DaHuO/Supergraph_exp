t = int(raw_input())


def find_face(s, f):
    for idx, i in enumerate(s):
        if i == f:
            return idx
    return -1


def flip(s, idx):
    for i in range(idx):
        if s[i] == '+':
            s[i] = '-'
        else:
            s[i] = '+'
    return s

for i in xrange(1, t + 1):
    s = list(raw_input())

    n_flips = 0

    while 1:
        c_face = s[0]

        if c_face == '+':
            idx = find_face(s, '-')
        else:
            idx = find_face(s, '+')

        if idx == -1:
            break

        s = flip(s, idx)
        n_flips += 1

    if s[0] == '-':
        flip(s, len(s))
        n_flips += 1

    print "Case #{}: {}".format(i, n_flips)
