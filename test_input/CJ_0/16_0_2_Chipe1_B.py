def ans(s):
    ans = 0
    curr = '+'
    while s:
        if s.pop() != curr:
            ans += 1
            curr = '-' if curr == '+' else '+'
    return ans

t=int(input())
for testcase in range(t):
    s = list(input())
    print("Case #{}: {}".format(testcase+1, ans(s)))
