
T = int(input())

for case in range(1, T+1):

    S = input()
    ans = ""
    for s in S:
        if ans+s >= s+ans:
            ans = ans + s
        else:
            ans = s + ans

    print("Case #%d: %s" % (case, ans))