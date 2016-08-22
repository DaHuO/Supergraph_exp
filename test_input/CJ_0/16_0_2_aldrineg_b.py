#!/usr/bin/python

import sys

def get_file(argv):
    if len(argv) == 1:
        return "b.in"
    else:
        return "b_%s.in" % (argv[1])

def get_file_out(argv):
    if len(argv) == 1:
        return "b.out"
    else:
        return "b_%s.out" % (argv[1])

def print_answer(t, answer, f):
    answer = "Case #%d: %s" % (t, answer)
    print answer
    f.write(answer)
    f.write("\n")

def all_happy(stack):
    for i in stack:
        if not i:
            return False
    return True

def min_flips(stack):
    flips = 0
    while not all_happy(stack) and flips < len(stack):
        flips = flips + 1
    return flips

def flip(stack, N):
    flipped = [not i for i in stack[N:]]
    flipped.reverse()
    # print 'flipped', flipped
    return stack[0:N] + flipped

def first_sad(stack):
    for i in xrange(0, len(stack)):
        if not stack[i]:
            return i
    return i

def brute(stack):
    min_flips = 0
    while not all_happy(stack):
        if stack[-1]:
            for i in xrange(len(stack)-1, -1, -1):
                if not stack[i]:
                    stack = flip(stack, i+1)
                    break
        else:
            for i in xrange(0, len(stack)):
                if not stack[i]:
                    stack = flip(stack, i)
                    break
        min_flips = min_flips + 1
    return min_flips

def main(argv):
    f = open(get_file(argv), 'r')
    f_out = open(get_file_out(argv), 'w')
    T = int(f.readline())
    for t in xrange(1, T+1):
        stack = [c == '+' for c in f.readline().replace('\n', '')]
        stack.reverse()
        last_number = brute(stack)
        print_answer(t, last_number, f_out)

if __name__ == "__main__":
    main(sys.argv)
