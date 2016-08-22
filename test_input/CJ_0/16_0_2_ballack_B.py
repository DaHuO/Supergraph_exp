import sys, re, math

if __name__ == "__main__":
    total = int(raw_input())
    for case in xrange(1, total + 1):
        pancake = raw_input()
        count = 0
        current = "+"
        for item in reversed(pancake):
            if item != current:
                current = item
                count += 1
        print "Case #{case}: {count}".format(**locals())
