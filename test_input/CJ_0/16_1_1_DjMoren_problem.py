'''
Created on Apr 16, 2016

@author: hduser
'''


def solve(s):
    winner = s[0]
    for i in xrange(1, len(s)):
        z = s[i]
        if winner + z > z + winner:
            winner += z
        else:
            winner = z + winner
    return winner


t = int(raw_input())
for i in xrange(1, t + 1):
    s = raw_input()
    print "Case #{}: {}".format(i, solve(s))
