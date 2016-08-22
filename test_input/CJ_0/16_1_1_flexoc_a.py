T = int(input())
for t in range(T):
    s = input()
    s2 = s[0]
    for i in range(1, len(s)):
        c = s[i]
        if ord(c) >= ord(s2[0]):
            s2 = c + s2
        else:
            s2 = s2 + c
    print("Case #%d: %s" % (t + 1, s2))
