def lastWord(word):
    res = word[0]
    for c in word[1:]:
        if c >= res[0]:
            res = c+res
        else:
            res = res + c

    return res

def solve(file):
    f = open(file, 'r')
    count = f.readline()
    case = 1
    for l in f.readlines():
        word = l.strip()
        print 'Case #%d: %s' % (case, lastWord(word))
        case += 1
    f.close()

solve('A-large.in')