
def last_word(s):
    words = [s[0]]
    for i in range(1, len(s)):
        new_words = []
        for w in words:
            new_words.append(s[i] + w)
            new_words.append(w + s[i])
        words = new_words

    return sorted(words)[-1]


T = int(raw_input())

for i in range(T):
    s = raw_input()
    print "Case #%s:" % str(i+1), last_word(s)
