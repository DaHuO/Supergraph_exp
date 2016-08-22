#!/usr/bin/env python

def get_number_of_flips(pancakes):
    flip = {'+': '-', '-': '+'}

    Q = []
    Q.append((pancakes, 0))
    seen = set([pancakes])

    while len(Q) != 0:
        v, d = Q.pop(0)
        
        if v.find('-') == -1: 
            return d

        for j in range(len(v) - 1, -1, -1):
            n = list(v)
            i = 0
            k = j
            while i <= k:
                n[i], n[k] = n[k], n[i]
                n[i] = flip[n[i]]
                if i != k:
                    n[k] = flip[n[k]]
                i += 1
                k -= 1
            x = ''.join(n)
            if x not in seen:
                seen.add(x)
                Q.append((x, d + 1))
                
if __name__ == '__main__':
    T = int(raw_input())
    for tc in range(1, T + 1):
        pancakes = raw_input()
        print 'Case #%d: %d' % (tc, get_number_of_flips(pancakes))
