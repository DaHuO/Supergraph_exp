#!/usr/bin/env python
# -*- coding: utf-8 -*-

def lastword(word):
    result = ""
    first_letter = ""
    count = 0
    for letter in word:
        if (count == 0):
            result = letter
            first_letter = letter
            count+=1
        else:
            if (letter >= first_letter):
                result = letter + result
                first_letter = letter
            else:
                result = result + letter
            count+=1

    return result

if __name__ == "__main__":
	testcases = input()

	for caseNr in xrange(1, testcases+1):
		word = raw_input()
		print("Case #%i: %s" % (caseNr, lastword(word)))