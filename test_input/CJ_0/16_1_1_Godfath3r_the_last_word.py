c = 1
for test in range(int(raw_input().strip())):
    last_word = []
    word = map(str, raw_input().strip().split(' '))
    last_word.append(str(word[0][0]))
    for i in xrange(1, len(word[0])):
        new_ = []
        for w in last_word:
            new_.append(''.join([word[0][i], w]))
            new_.append(''.join([w, word[0][i]]))
        last_word = new_[:]
    print 'Case #{}: {}'.format(c, sorted(last_word)[-1])
    c += 1

