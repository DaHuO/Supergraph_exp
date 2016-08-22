for t in range(1, int(input())+1):
    s = input().strip(" ")

    i = 1
    result = s[0]
    while i < len(s):
        if result[0] <= s[i]:
           result = s[i] + result
        else:
            result += s[i]
        i += 1

    print("Case #{0}: {1}".format(t, result))

