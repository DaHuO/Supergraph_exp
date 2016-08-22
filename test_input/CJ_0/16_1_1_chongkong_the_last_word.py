def solve(s):
    ans = s[0]
    for c in s[1:]:
        ans = c + ans if c >= ans[0] else ans + c
    return ans


def main():
    t = int(input())
    for i in range(t):
        print('Case #{}: {}'.format(i + 1, solve(input())))


main()