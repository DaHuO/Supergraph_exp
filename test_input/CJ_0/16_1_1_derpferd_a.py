import math
import sys
from copy import deepcopy as copy

fpIn = open("ex.in", "r")
fpOut = open("ex.out", "w")
# fpIn = open("a.in", "r")
# fpOut = open("a.out", "w")
# fpIn = open("a.in", "r")
# fpOut = open("a.out", "w")

def raw_input():
    return fpIn.readline().strip()

class Print(object):
    def __init__(self, f):
        self.f = f

    def write(self, text):
        fpOut.write(text)
        self.f.write(text)

    def flush(self):
        fpOut.flush()
        self.f.flush()

def put(s):
    sys.stdout.write(s)

def get_combs(s):
    cs = [s[0]]
    for c in s[1:]:
        ncs = []
        for t in cs:
            ncs += [c+t, t+c]
        cs = ncs
    return cs

# return a string with the answer in it.
def do_test():
    s = ""
    word = raw_input()
    #print >> sys.stderr, get_combs(word), word
    words = get_combs(word)

    return list(sorted(words))[-1]


def main():
    line = raw_input()
    num_tests = int(line)
    for i in range(num_tests):
        print "Case #" + str(i+1) + ": " + do_test()

if __name__ == '__main__':
    if not isinstance(sys.stdout, Print):
        sys.stdout = Print(sys.stdout)
    main()