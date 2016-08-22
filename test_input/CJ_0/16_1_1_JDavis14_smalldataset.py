t = int(raw_input())
for i in xrange(1, t + 1):
    S = raw_input()
    last_word = S[0]
    for character in S[1:]:
        if character >= last_word[0]:
            last_word = character + last_word
        else:
            last_word += character

    print "Case #{}: {}".format(i, last_word)
