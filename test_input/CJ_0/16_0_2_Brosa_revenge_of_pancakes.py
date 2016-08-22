#-*- coding: utf-8 -*-
t = int(input())

# Runtime: O(n) where `n` is number of pancakes
for i in range(t):
    seq = input()

    if seq.count('-') == 0:
        print('Case #%d: %d' % (i + 1, 0))
        continue

    happy = 0
    blank = 0
    for c in seq:
        if c == '+':
            happy = min(happy, blank + 1)
            blank = min(blank + 2, happy + 1)
        else:
            happy = min(happy + 2, blank + 1)
            blank = min(blank, happy + 1)
    print('Case #%d: %d' % (i + 1, happy))
