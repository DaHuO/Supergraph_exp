import fileinput
test_file = fileinput.input()
num_tests = int(next(test_file).strip())
for i in xrange(num_tests):
    orig = list(next(test_file).strip())
    word = ""
    for c in orig:
        if 0 < len(word) and c == word[0]:
            word = c + word
        elif c < word:
            word = word + c
        else:
            word = c + word
    print "Case #%d: %s" % (i + 1, word)
