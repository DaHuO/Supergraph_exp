import re

infile = "/Users/Christopher/Downloads/A-large.in-2.txt"
outfile = "/Users/Christopher/Desktop/Python/CodeJam/practice.out.txt"
txt = open(infile)
data = txt.read()
lines = [l for l in re.split('\n+', data) if l][1:]

newlines = []
for i,l in enumerate(lines):
    line = "Case #" + str(i+1) +": "
    letters = [l[0]]
    for c in l[1:]:
        if c >= letters[0]: letters = [c] + letters
        else: letters = letters + [c]

    newlines.append(line + ''.join(letters))

lines = '\n'.join(newlines)

target = open(outfile, 'w')
target.write(lines)