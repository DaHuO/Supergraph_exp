import sys

tests = int(sys.stdin.readline())

def isDone(plate):
    for c in plate:
        if c == "-":
            return False
    return True

def minus(plate):
    for it in xrange(len(plate) - 1, -1, -1):
        if plate[it] == "-":
            return it

for test in xrange(tests):
    plate = list(sys.stdin.readline().rstrip())

    ans = 0
    if not isDone(plate):
        ans = 1
        limit = minus(plate) + 1
        curr = plate[0]
        for it in xrange(limit):
            if plate[it] != curr:
                ans += 1
                curr = plate[it]

    print "Case #" + str(test + 1) + ": " + str(ans)
