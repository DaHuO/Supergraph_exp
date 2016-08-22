output = "Case #{}: {}"

for x in xrange(int(raw_input())):
    word = raw_input().strip()
    new_word = "" + word[0]
    for y in word[1:]:
        if y >= new_word[0]:
            new_word = y + new_word
        else:
            new_word += y
    print output.format((x+1), new_word)
