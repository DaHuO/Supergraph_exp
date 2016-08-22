
T = int(input())

for t in range(T):
    letters = str(input())

    word = letters[0]
    for i, l in enumerate(letters):
        if (i == 0):
            continue
        if l < word[0]:
            word = word + l
        else:
            word = l + word;

    print("Case #"+str(t+1)+": "+word)