T = int(input())
for t in range(1, T+1):
    word = input()
    output = word[0]
    last = word[0]
    for x in word[1:]:
        if ord(x) >= ord(last):
            output = x + output
            last = x
        else:
            output = output + x
    print("Case #{0}: {1}".format(t, output))
