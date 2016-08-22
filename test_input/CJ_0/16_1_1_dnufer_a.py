import sys

T = int(sys.stdin.readline())

for t in xrange(T):
    s = sys.stdin.readline().strip()

    last_word = s[0]
    for c in s[1:]:
        if ord(c) < ord(last_word[0]):
            last_word += c
        else:
            last_word = c + last_word

    print "Case #%d:" % (t + 1), last_word
