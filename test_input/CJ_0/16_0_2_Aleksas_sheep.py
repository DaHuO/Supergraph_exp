# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
p='+'
m='-'
for i in range(1, t + 1):
    prev="none"
    groups=0
    for s in input():
        if (s==prev):
            continue
        else:
            groups+=1
            prev=s
    if (s==p):
        groups -=1

    print("Case #{}: {}".format(i, groups))
