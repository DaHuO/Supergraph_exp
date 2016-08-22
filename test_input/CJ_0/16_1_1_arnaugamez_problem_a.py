t = int(raw_input())
for i in xrange(1, t + 1):

    S = raw_input()
    last_word = S[0]
    for c in S[1:]:
        if max(c, last_word[0]) == c:
            last_word = c + last_word
        else:
            last_word = last_word + c


    print "Case #{}: {}".format(i, last_word)