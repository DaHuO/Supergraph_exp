__author__ = 'dilip'

def findlastword(s):
    lastwordlist = [s[0]]
    for i in range(1, len(s)):
        if s[i] >= lastwordlist[0]:
            lastwordlist.insert(0, s[i])
        else:
            lastwordlist.append(s[i])
    return ''.join(lastwordlist)



with open('A-large.in') as in_file:
    t = int(in_file.readline())
    with open('A-large.out', 'w') as out_file:
        for i in xrange(1, t+1):
            s = in_file.readline().strip()
            lastword = findlastword(s)
            out_file.write('Case #{0}: {1}\n'.format(i, lastword))