
flip = lambda s: ''.join('+' if c == '-' else '-' for c in s[::-1])
def nflips(str):
    if '-' not in str: return 0
    
    firstd = str.find('-')
    lastd = str.rfind('-')
    firstu = str.find('+')
    
    if firstd:
        str = flip(str[firstd:lastd+1])
        return nflips(str) + 2
        
    str = flip(str[firstu:lastd+1])
    return nflips(str) + 1

import re

infile = "/Users/Christopher/Downloads/B-large.in.txt"
outfile = "/Users/Christopher/Desktop/Python/CodeJam/practice.out.txt"
txt = open(infile)
data = txt.read()
lines = [l for l in re.split('\n+', data) if l][1:]

newlines = []
for i,l in enumerate(lines):
    line = "Case #" + str(i+1) +": "
    line += str(nflips(l))
    newlines.append(line)

lines = '\n'.join(newlines)

target = open(outfile, 'w')
target.write(lines)
