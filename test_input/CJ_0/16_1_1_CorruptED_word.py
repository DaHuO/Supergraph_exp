import sys

def last_word(s):
    word = [s[0]]
    s = s[1:]
    for c in s:
        if word[0] > c:
            word.append(c)
        else:
            word.insert(0, c)

    return ''.join(word)

if __name__ == "__main__":
    num_cases = int(sys.stdin.readline())

    for i in xrange(num_cases):
        s = sys.stdin.readline()
        word = last_word(s.strip())
        print "Case #{0}: {1}".format(i + 1, word)
