#/usr/bin/env python
# Google Code Jam Round 1A 2016
# A. The Last Word
# https://code.google.com/codejam/contest/4304486/dashboard

def process(string):
    letter = max(string)
    c = string.count(letter)
    i = string.index(letter)
    string = string.replace(letter, '')
    if len(string[:i]) == 0:
        return c*letter+string[i:]
    return c*letter+process(string[:i])+string[i:]

t = int(raw_input())
for i in xrange(t):
    print 'Case #%d: %s' % (i+1, process(raw_input()))
