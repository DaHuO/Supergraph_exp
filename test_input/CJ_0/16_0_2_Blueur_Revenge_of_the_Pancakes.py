import sys

inputFile = sys.argv[1]

f = open(inputFile, 'r')

args = f.readline()
T = int(args)

def countChange(ls):
    last = ls[0]
    count = 0
    for l in ls[1:]:
        if (last != l):
            count = count + 1
            last = l
    return count

def answer(input):
    ls = list(input)
    if (ls[-1] == '-'):
        return countChange(ls) + 1
    else:
        return countChange(ls)

for t in range(T):
    n = f.readline().replace('\n', '')
    print("Case #{0}: {1}".format(t+1, answer(n)))