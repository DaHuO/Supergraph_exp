t = int(input())
for i in range(1, t + 1):
    n = list(input())
    word = ""
    for char in n:
        if char + word > word + char:
            word = char + word
        else:
            word = word + char
    print("Case #" + str(i) + ": " + word)



