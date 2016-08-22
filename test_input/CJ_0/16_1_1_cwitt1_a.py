import string

T = int(input())

for i in range(1, T + 1):
    s = input()
    w = s[0]

    for c in s[1:]:
        if c < w[0]:
            w += c
        else:
            w = c + w

    print("Case #{}: {}".format(i, w))
