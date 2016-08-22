from redef_io import *


def sort_str(s=''):
    return ''.join(reversed(sorted(s)))


def get_highest(s=''):
    new_s = s[0]

    for i in range(1, len(s)):
        c = s[i]
        if ord(c) < ord(new_s[0]):
            new_s = new_s + c
        else:
            new_s = c + new_s

    return new_s

t = int(input())

for it in range(t):
    s = input().strip()

    print_file(get_highest(s))
