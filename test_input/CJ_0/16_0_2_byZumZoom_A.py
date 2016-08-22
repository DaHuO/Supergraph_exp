
with open('in.txt') as in_f, open('out.txt', 'w') as out_f:
    n = in_f.readline()
    case = 0
    for line in in_f.readlines():
        case += 1
        s = line[:-1]
        last = s[0]
        ans = 1
        for c in s[1:]:
            if c == last:
                continue
            else:
                ans += 1
                last = c
        if last == '+':
            ans -= 1
        print("Case #{}: {}".format(case, ans), file=out_f)
