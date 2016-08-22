

def parse(f):
    with open(f, 'r') as c:
        lines = c.readlines()
    lines = [list(line.strip()) for line in lines]
    return lines[1:]


def flip(l):
    to_flip = list(l)
    for i in range(len(to_flip)):
        if to_flip[i] == '-':
            to_flip[i] = '+'
        else:
            to_flip[i] = '-'
    to_flip = to_flip[::-1]
    return to_flip


def changes(s):
    change = 0
    for i, e in enumerate(s[1:]):
        if s[i] != e:
            change += 1
    return change


def rank_last(s):
    for j in range(len(s)-1, -1, -1):
        if s[j] == '-':
            return j


def solve(s):
    print('Using', s)
    if '-' not in s:
        return 0
    else:
        n = 0
        while '-' in s:
            if changes(s) == 0:
                return n+1
            m = changes(s)
            ind = 0
            for i in range(len(s)-1):
                c = changes(flip(s[:i+1]) + s[i+1:])
                if c < m:
                    m = c
                    ind = i
            s = flip(s[:ind+1]) + s[ind+1:]
            n += 1
        return n

if __name__ == "__main__":
    inputs = parse('B-large.in')
    print(inputs)
    with open('ans.txt', 'w') as ans:
        for ind, i in enumerate(inputs):
            ans.write('Case #%d: %s\n' % (ind+1, solve(i)))
