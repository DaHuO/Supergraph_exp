import os
import sys

def get_valid_idx(s):
    i = 1
    lens = len(s)
    while i <= lens:
        if s[-i] == '+':
            i += 1
        else:
            break
    return i

def flip(s, idx):
    lens = len(s)
    for i in xrange(lens-idx+1):
        s[i] = '+' if s[i] == '-' else '-'
   
if __name__ == '__main__':
    #T = int(raw_input().strip())
    with open('B-large.in', 'r') as f:
        T = int(f.readline().strip())
        for i in xrange(T):
            s = list(f.readline().strip())
            #s = list(raw_input().strip())
            res = 0
            idx = get_valid_idx(s)
            lens = len(s)
            while idx != lens + 1:
                res += 1
                flip(s, idx)
                idx = get_valid_idx(s)
            print 'Case #%s: %s' % (i+1, res)
    


