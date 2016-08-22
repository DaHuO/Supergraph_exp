from collections import defaultdict
import sys

def flip(l, n):
    """
    Flips n of the top pancakes in l
    """
    flipee = l[0:n]
    static = l[n:]
    flipee = [not x for x in reversed(flipee)]
    return flipee + static

def normalize(s):
    return [True if c == '+' else False for c in s]

def simplify(l):
    """
    Removes irrelevant parts of the stack because they're already in
    a good state
    """
    length = len(l)
    for i, p in enumerate(reversed(l)):
        if not p:
            return l[0:length - i]
    else:
        return []

def analyze(l):
    """
    Determines correct place to flip
    """
    if not l[0]: # If we have stuff up front, flip the whole thing to remove
        return len(l)
    for i, p in enumerate(l):
        if not p:
            return i

def solve(s):
    l = normalize(s)
    i = 0
    while 1:
        l = simplify(l)
        if not l:
            break
        n = analyze(l)
        l = flip(l, n)
        i += 1
    return i

if __name__ == "__main__":
    num_cases = int(sys.stdin.readline())

    for i in xrange(num_cases):
        s = sys.stdin.readline()
        number = solve(s.strip())
        print "Case #{0}: {1}".format(i + 1, number)
