def flip(l, end):
    i = 0
    while i < end:
        if l[i] == '+':
            l[i] = '-'
        else:
            l[i] = '+'
        i += 1

    l1 = l[:end]
    l1.reverse()
    l2 = l[end:]

    return (l1 + l2)

t = int(input())
for i in range(1, t + 1):
    l = list(input())
    c = 0
    cont = 1
    while cont:
        if l[0] == '+':
            j = 1
            while j < len(l) and l[j] != '-':
                j += 1
            if j == len(l):
                cont = 0
            else:
                l = flip(l, j)
                c += 1
        else:
            j = len(l) - 1
            while l[j] != '-':
                j -= 1
            flip(l, j + 1)
            c += 1

    print("Case #{}: {}".format(i, c))
    # check out .format's specification for more formatting options
