def insert_letter(c, word):
    if word == "":
        return word + c
    if c >= word[0]:
        return c + word
    else:
        return word + c


def last_word(word):
    new_word = ""
    for c in word:
        # print new_word
        new_word = insert_letter(c, new_word)

    return new_word


f = open("input.txt", "r+")
lines = tuple(f)

with open("output.txt", "w+") as o:
    for i in range(1, len(lines)):
        o.write("Case #%d: %s\n" % (i, last_word(lines[i].strip())))
