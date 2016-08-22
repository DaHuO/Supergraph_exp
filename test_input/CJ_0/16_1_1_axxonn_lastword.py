t = int(raw_input())
for case in range(1, t+1):
    s = raw_input()
    word = s[0]
    for c in s[1:]:
        if c >= word[0]: # >= vs > is crucial!
            word = c + word
        else:
            word = word + c
    print "Case #%d: %s" % (case, word)
