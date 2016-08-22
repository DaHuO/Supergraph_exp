t = int(input())
for c in range(t):
    s = input()
    out = s[0]
    for char in s[1:]:
        if ord(out[0]) <= ord(char):
            out = char + out
        else:
            out = out + char
    print("Case #" + str(c+1) + ": " + out)
        