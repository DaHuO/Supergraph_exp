T = int(input())
for t in range(1, T+1):
    s = input()

    front = [s[0]]
    back = []

    for index in range(1, len(s)):
        if s[index] >= front[-1]:
            front.append(s[index])
        else:
            back.append(s[index])

    print("Case #{}: {}".format(t, ''.join(front[::-1] + back)))