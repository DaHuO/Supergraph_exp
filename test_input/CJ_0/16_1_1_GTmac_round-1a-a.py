t = int(raw_input())
for case_num in range(1, t + 1):
    s = raw_input()
    res = ''
    for i, ch in enumerate(s):
        if i == 0:
            res += ch
        else:
            if (res + ch > ch + res):
                res = res + ch
            else:
                res = ch + res
    print 'Case #%d: %s' % (case_num, res)
