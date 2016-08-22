#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solve(cipher):
    word = []
    word.insert(0, cipher[0])
    size = len(cipher)
    for i in range(1, size):
        if ord(cipher[i]) >= ord(word[0]):
            word.insert(0, cipher[i])
        else:
            word.append(cipher[i])
    return ''.join(word)

if __name__ == "__main__":
    testcases = input()

    for caseNr in xrange(1, testcases + 1):
        cipher = raw_input()
        print("Case #%i: %s" % (caseNr, solve(cipher)))
