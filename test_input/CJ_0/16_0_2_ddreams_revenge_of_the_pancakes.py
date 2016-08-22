#!/usr/bin/python

import os
import sys
import string
import re


def process (text):

	s = ""

	lines = text.split("\n")
	while "" in lines:
		lines.remove("")

	N = None
	i = 1
	for line in lines:
		#print line
		if i == 0:
			pass
		elif i == 1:
			N = str(line)
		else:
			#print ">>>>> " + str(i) + " -> " + line
			pila = line
			r = calc(pila)
			s += "Case #%d: %s\n" % (i-1, r)
		i += 1

	return s


def calc (pila):

	p = pila

	n = 0
	while True:
		try:
			j = p.index("-")
		except:
			break
		t = p[0]
		#print len(p)
		if len(p) == 1:
			n += 1
			break
		else:
			for i in range(1, len(p)):
				if t != p[i]:
					break
			#print "i: " + str(i)
			if i == len(p)-1:
				p = p[:i][::-1].replace("+", "n").replace("-", "+").replace("n", "-")
			else:
				np = p[:i][::-1].replace("+", "n").replace("-", "+").replace("n", "-")
				p = np + p[i:]
			#print p
		n += 1
	#print "n: " + str(n)

	return n


if __name__ == "__main__":

	( inputfile, ) = sys.argv[1:]

	inpt = """5
-
-+
+-
+++
--+-"""

	inpt = open(inputfile, "r").read()
	outputfile = inputfile + ".out"
	out = process(inpt)
	outpt = open(outputfile, "w")
	outpt.write(out)
	outpt.close()

	#for i in (5, 0, 1, 2 , 11, 1692):
	#	print ">>>>>> %d" % i
	#	print calc(i)

