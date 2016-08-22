from sys import argv, stdin

def get_last_word(word):
    if len(word) == 1:
        return word
    result = [word[0]]
    for i in xrange(1, len(word)):
        if word[i] >= result[0]:
            result.insert(0, word[i])
        else:
            result.append(word[i])
    return ''.join(result)


if __name__ == '__main__':
    with (open(argv[1]) if len(argv) == 2 else stdin) as f:
        inputs = int(f.readline())
        for i in xrange(inputs):
            last = get_last_word(f.readline().strip())
            print "Case #%i: %s" % (i+1, last)
