import sys
sys.setrecursionlimit(10000)

def find_res(Sa):
    if len(Sa) == 1:
        return list(Sa)
    sub = find_res(Sa[:-1])
    last_C = Sa[-1]
    if last_C >= sub[0]:
        return [last_C] + sub
    return sub + [last_C]

with open("in") as f:
    T = int(f.readline())
    for t in xrange(T):
        S = f.readline()[:-1]
        res = find_res(list(S))
        print "Case #{}: {}".format(t + 1, "".join(res))
