import numpy as np

def output(i, out):
    with open('A-large.out', 'a') as outfile:
        outfile.write("Case #{0}: {1}".format(i, out))

def solve(i, line): 
    outstring = []
    for j, char in enumerate(str(line)):
        if j == 0:
            outstring.append(char)
        else:
            if ord(char) >= ord(outstring[0]):
                outstring.insert(0, char)
            else:
                outstring.append(char)
    output(i, ''.join(outstring))

lines = open('A-large.in').readlines()

for i, line in enumerate(lines):
    if i > 0:
        solve(i, line)