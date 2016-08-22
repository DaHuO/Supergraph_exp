def q2(s):
    flips, current = 1 if s[-1] == '-' else 0, s[0]
    for i in s:
        if i == current:
            continue
        else:
            flips += 1
            current = '-' if current == '+' else '+'
    return flips

T = int(input())
for i in range(T):
    s = input()
    print('Case #%s: %s' % (i + 1, q2(s)))