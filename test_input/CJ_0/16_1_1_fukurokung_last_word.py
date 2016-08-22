#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#Problem A: The Last Word
#Author: Wongnaret Khantuwan

def lastword(txt):
    result = ''

    for char in txt:
        if len(result) == 0:
            result+=char
        elif char >= result[0]:
            result = char+result
        else:
            result+=char

    return result

#main function
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
  input = raw_input()
  print "Case #%d: %s" % (i, lastword(input))

