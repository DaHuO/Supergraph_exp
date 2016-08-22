from os import getenv
from sys import argv, stdin

def debug(s, log):
    if getenv('DEBUG'):
        print s, log


def flip(pancakes, pos):
    if pos >= len(pancakes):
        raise ('Invalid range: %d out of %d' % (pos, len(pancakes)))
    stack = []
    i = 0
    while i <= pos:
        flipped = '+' if pancakes[i] == '-' else '-'
        stack.append(flipped)
        i += 1

    out = ''
    # pop from the stack
    while len(stack):
        out += stack.pop()
    # append the rest
    for i in xrange(pos+1, len(pancakes)):
        out += pancakes[i]

    debug('FLIP', out)

    return out

def get_answer(n, i=0):
    # fm = find the first -
    # if (any + before fm) then
    #    flip everything before + including
    # while (contains -)
    #    mp = find the last -
    #    flip everything before mp including mp itself

    if len(set(n)) == 1 and n[0] == '+':
        return i

    fm = n.find('-')
    fp = n.rfind('+', 0, fm)
    lm = n.rfind('-')
    if fp > -1 and fp < fm:
        n = flip(n, fp)
        i += 1
    n = flip(n, lm)
    return get_answer(n, i+1)

if __name__ == '__main__':
    with (open(argv[1]) if len(argv) == 2 else stdin) as f:
        inputs = int(f.readline())
        for i in xrange(inputs):
            n = f.readline().strip()
            answer = get_answer(n, 0)
            print "Case #%i: %s" % (i+1, answer)

# +-+
# --+
# +++

# +-+-
# --+-
# +-++
# --++
# ++++

# -+-+
# +-++
# --++
# ++++

# --+-
# +-++
# --++
# ++++

