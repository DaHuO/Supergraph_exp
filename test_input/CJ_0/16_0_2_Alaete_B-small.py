infile = open("B-large.in", "r")
cases = infile.readline()
lines = infile.readlines()

stacks = []
flips = []

for line in lines:
    line = line.rstrip()
    stacks.append(line)
infile.close()

def Number_Of_Types_And_Bottom(stack):
    types = 1
    stack = list(stack)
    for i in range(1, len(stack)):
        if stack[i-1] != stack[i]:
            types += 1
    bottom = stack[-1]
    return types, bottom

outfile = open("B-large-output.txt", "a")
for i in range(len(stacks)):
    types = Number_Of_Types_And_Bottom(stacks[i])[0]
    bottom = Number_Of_Types_And_Bottom(stacks[i])[1]
    if bottom == "+":
        answer = types - 1
    else:
        answer = types
    outfile.write("Case #%s: %s\n" % (i+1, answer))
outfile.close()