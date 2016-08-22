t = int(input())
for case in range(t):
    s = input()
    ans = 0
    prev = 'x'
    for c in s:
        if c != prev:
            ans += 1
            prev = c
    if s[-1] == '+':
        ans -= 1
    print('Case #', case + 1, ': ', ans, sep = '')
