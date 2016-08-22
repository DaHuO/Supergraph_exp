def give_the_word(x, word):
    res = "" + word[0]
    for i in range(1, len(word)):
        if(word[i] < res[0]):
            res = res + word[i]
        else:
            res = word[i] + res
    fil = open("out.txt", "a")
    fil.write("Case #{0}: {1}".format(x+1, res))


f = open("in.in", "r")
T = f.readline()
for j in range(int(T)):
    x = j
    word = f.readline()
    give_the_word(x, word)
