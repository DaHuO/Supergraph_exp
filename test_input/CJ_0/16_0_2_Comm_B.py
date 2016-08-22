import numpy as np

def output(i, out):
    with open('B-large.out', 'a') as outfile:
        outfile.write("Case #{0}: {1}\n".format(i, out))

def solve(i, stack):                
    cursymbol = stack[0]
    counter = 0 if stack[-1] == "+" else 1
    for symbol in stack:
        if symbol != cursymbol:
            cursymbol = symbol
            counter += 1
    output(i, counter)

lines = np.loadtxt('B-large.in', dtype=str)

for i, line in enumerate(lines):
    if i > 0:
        solve(i, line)