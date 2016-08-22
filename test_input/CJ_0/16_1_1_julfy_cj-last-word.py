from sets import Set

def scan(s):
    biggest = ""
    last = []
    for c in s:
        if c >= biggest:
            biggest = c
            last.insert(0, c)
        else:
            last.append(c)
    return ''.join(last)

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    n = raw_input()
    #n,m = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    print "Case #{}: {}".format(i,scan(n))
    # check out .format's specification for more formatting options
