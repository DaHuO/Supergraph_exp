__author__ = 'dhinesh'


def solve(pattern):
    if pattern.find('-') == -1:
        return 0
    elif pattern.find('+') == -1:
        return 1
    else:
        pattern = list(pattern)
        count = 0
        pattern = pattern[:find_negative(pattern)+1]
        while len(pattern) > 0:
            if pattern[0] == '-':
                pattern = flip(pattern)
                count += 1
            else:
                pattern = flip_positive(pattern)
                pattern = flip(pattern)
                count += 2
            pattern = pattern[:find_negative(pattern)+1]
        return count


def flip(pattern):
    for i in range(len(pattern)):
        if pattern[i] == '-':
            pattern[i] = '+'
        else:
            pattern[i] = '-'
    return pattern[::-1]


def flip_positive(pattern):
    for i in range(len(pattern)):
        if pattern[i] == '-':
            break
        else:
            pattern[i] = '-'
    return pattern

def find_negative(pattern):
    for i in range(len(pattern)-1, -1, -1):
        if pattern[i] =='-':
            return i
    return -1

def run_program():
    t = int(raw_input())
    for i in xrange(1, t + 1):
        pattern = raw_input()
        print "Case #{0}: {1}".format(i, solve(pattern))


if __name__ == '__main__':
    run_program()