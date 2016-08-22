import sys
import itertools

def getWords(line):
    winner = line[0]
    for i, ch in enumerate(line[1:]):
        winner = winner + ch if ch >= winner[-1] else ch + winner

    return winner[::-1]

def lastword(T):
    lines = open(T).read().split('\n')
    num = int(lines[0])

    for i in xrange(1, num+1):
        winner = getWords(lines[i])
        print "Case #" + str(i) + ': ' + winner


if __name__ == '__main__':
    lastword(sys.argv[1])
