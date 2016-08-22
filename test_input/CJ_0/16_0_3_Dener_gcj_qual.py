#!/usr/bin/python

import progressbar
import sys

def check(number):
    iter_count = 0;
    res = []
    for base in xrange(2, 11):
        buf = number
        result = 0
        append = 1
        while buf > 0:
            if buf % 2 == 1:
                result += append
            append *= base
            buf /= 2

        divisor = 2
        found = False
        while divisor * divisor <= result:
            iter_count += 1
            if iter_count > 10000:
                return None
            #print >> sys.stderr, base, divisor
            if result % divisor == 0:
                res.append(divisor)
                found = True
                break
            divisor += 1
        if not found:
            return None
    return res

sys.stdin.readline()
N, J = map(int, sys.stdin.readline().strip().split())

print "Case #1:"
found_cnt = 0
#bar = progressbar.ProgressBar()
#bar.start()
for q, cur_number in enumerate(xrange(2**(N-1) + 1, 2**(N), 2)):
    #bar.update(q)
    #print >> sys.stderr, cur_number
    res = check(cur_number)
    if res is not None:
        #print >> sys.stderr, 'found'
        found_cnt += 1
        print "{0:b}".format(cur_number), ' '.join(map(str, res))
        if found_cnt == J:
            sys.exit(0)
#bar.finish()
