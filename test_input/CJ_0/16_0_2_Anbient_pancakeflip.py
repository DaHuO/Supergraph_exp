#!/usr/bin/env python
# -*- coding: utf-8 -*-

def pancakeflip(array):
    count = 0
    last_dir = None


    for i in xrange(0, len(array)):
        if last_dir is None:
            last_dir = array[0]
            #print ("initialize %c" % last_dir)
        else:
            if (array[i] != last_dir):
                count += 1
                last_dir = array[i]

    if (last_dir == '-'):
        count += 1

    return count




if __name__ == "__main__":
	testcases = input()
	for caseNr in xrange(1, testcases+1):
		cipher = raw_input()
		count = pancakeflip(list(cipher))
		print("Case #%i: %s" % (caseNr, count))
