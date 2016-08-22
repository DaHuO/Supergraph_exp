for t in range(int(input())):
    s = input().strip()
    last = s[0]
    changes = 0
    for c in s:
        if c != last:
            changes += 1
            last = c
    if last == '-':
        changes += 1
    print('Case #{}: {}'.format(t+1, changes))
