t = int(input())
for i in range(1, t+1):
    print("Case #", i, ": ", sep='', end='')
    s = list(input().strip())
    cnt = 0
    while len(s):
        while len(s) and s[-1] == '+':
            s = s[:-1]
        if not len(s):
            break
        cnt += 1
        if s[0] == '-':
            s = s[::-1]
            for i in range(len(s)):
                if s[i] == '-':
                    s[i] = '+'
                else:
                    s[i] = '-'
            continue
        for i in range(len(s)):
            if s[i] == '-':
                break
            else:
                s[i] = '-'
    print(cnt)
