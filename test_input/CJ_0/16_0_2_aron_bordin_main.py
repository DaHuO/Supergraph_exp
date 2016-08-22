def reverse_sublist(lst, start, end):
    for i in range(start, end):
        lst[i] = '+' if lst[i] == '-' else '-'
    lst[start:end] = lst[start:end][::-1]
    return lst

for t in range(int(input())):
    p = list(input())
    r = len(p)
    m = r
    it = 0
    while True:
        if p[0] == '+':
            k = None
            for i in range(1, r):
                if p[i] == '-':
                    k = i
                    reverse_sublist(p, 0, i)
                    break
            if k is None:
                break
        else:
            k = 0
            for i in range(1, m):
                if p[i] == '-':
                    k = i
            reverse_sublist(p, 0, k + 1)
            m = k + 1
        it += 1

    print('Case #%d: %d' % (t + 1, it))
