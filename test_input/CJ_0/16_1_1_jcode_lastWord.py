__author__ = 'Justin'

w = "CAB"


def prepend(l, s):
    return l+s

def append(l, s):
    return s+l

num_tests = int(raw_input())
for x in xrange(1, num_tests+1):
    w = raw_input()
    first = w[0]
    rest = w[1:]
    words = list(first)

    for letter in rest:
        ws = []
        for word in words:
            ws.append(prepend(letter, word))
            ws.append(append(letter, word))
        words = ws

    last = sorted(words)[-1]
    print "Case #{}: {}".format(x, last)

