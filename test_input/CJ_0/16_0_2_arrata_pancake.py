import sys

n = int(sys.stdin.readline())

def flip(s):
    ret = ''
    for x in s[::-1]:
        if x == '+':
            ret += '-'
        else:
            ret += '+'
    return ret


def flipper(s):
    checker = True
    back = 0
    for i,x in enumerate(s):
        if x == '-':
            checker = False
            back = i
            break
    if checker:
        return 0
    else:
        checkstring = s[back:]
        ret = 0
        checker = True
        #the first string is always a -
        while True:
            checker = True
            if flip(checkstring)[0] == checkstring[0]:
            #    checkstring = checkstring[0] + flip(checkstring[1:])
                i = 1
                while(checkstring[i] == flip(checkstring[i:])[0]):
                    i += 1
                checkstring = checkstring[:i] + flip(checkstring[i:])
            else:
                checkstring = flip(checkstring)
            ret += 1
            #print checkstring
            for i, x in enumerate(checkstring):
                if x == '-':
                    checker = False
                    checkstring = checkstring[i:]
                    break
        #    print checkstring, checker
            if checker:
                break
        return ret

    #    while True:



for i in range(n):
    s = sys.stdin.readline().strip()
    print "Case #%d:" % (i + 1), flipper(s[::-1])
