#!/usr/bin/env python

# Contestant: Veselin 'anrieff' Georgiev
# Round: Google Code Jam Qualification 2016
# Task: B. Revenge of the pancakes
# Solution: Greedy. At each step, find the largest single-colored block at the top, and flip it, until we finish.

TC = int(raw_input().strip())

for tc in xrange(1, TC + 1):
	print "Case #%d:" % tc, 
	a = list(raw_input().strip())
	n = len(a)
	steps = 0
	while a.count('-') != 0:
		steps += 1
		i = 0
		while i < n and a[i] == a[0]:
			i += 1
		for j in xrange(i):
			a[j] = '-' if a[j] == '+' else '+' # reverse
	print steps
