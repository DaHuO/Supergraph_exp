def last_word(s):
    word = [s[0]]
    s = s[1:]
    for c in s:
        if c >= word[0]:
            word.insert(0, c)
        else:
            word.append(c)
    return ''.join(word)

if __name__ == '__main__':
    for T in range(int(raw_input().strip())):
        s = raw_input().strip()
        print "Case #%d: %s" % (T+1, last_word(s))