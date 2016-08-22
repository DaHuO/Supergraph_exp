#!/usr/bin/env python


def last_word(s):
    out = s[0]
    for c in s[1:]:
        if c >= out[0]:
            out = c + out
        else:
            out += c
    return out

def main():
    T = int(raw_input())
    for i in range(T):
        print 'Case #%s: %s' % (i+1, last_word(raw_input()))

if __name__ == "__main__":
    main()
