def flip(n, l):
    """
    Flips the first n pancakes
    """
    lst = l
    if (len(lst) < n + 1):
        # TODO: throw err here
        raise "err"
    else:
        toFlip = lst[0:(n + 1)]
        rest = lst[(n + 1):]
        flipped = map(lambda p: '-' if p is '+' else '+', toFlip)
        flipped.reverse()
        return (flipped + rest)


def allHappy(lst):
    """ True if all are happy in lst"""
    return reduce(lambda x, y: x and y, [True if x is '+' else False for x in lst])


def findBottomMostUnhappy(l):
    """ Returns the number of the bottom most unhappy pancake """
    count = 0
    i = 0
    for c in lst:
        if c is '-':
            count = i
        i += 1
    return count


def isEqual(l0, l1):
    for c0 in l0:
        for c1 in l1:
            if (c0 != c1):
                return False
    return True


def findNumFlips(lst):
    """
    Find the first pancake that is different and flip all the same one's before it so a certain the prefix of string has same characters. keep doing this till all are same. if all are - then flip all else all will be +
    """
    count = 0
    while not allHappy(lst):
        if len(lst) == 1:
            lst = flip(0, lst)
            count += 1
        else:
            nxt = 0
            ind = 1
            while lst[0] == lst[ind]:
                nxt += 1
                ind += 1
                if ind >= len(lst):
                    # all are same && word is unhappy -> all must be "-"
                    # flip all
                    ind = len(lst) - 1
                    break
            # print "flipping num:", nxt
            lst = flip(nxt, lst)
            count += 1
    return count


t = int(raw_input())
for i in xrange(1, t + 1):
    str = raw_input()
    lst = [c for c in str]
    # print "input"
    # print "before::", lst
    # print "after::", flip(2, [ "-","-","+","-" ])
    print "Case #{}: {}".format(i, findNumFlips(lst))
