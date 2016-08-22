#!/usr/bin/python
"""
Google Code Jam 2016
Problem B. Revenge of the Pancakes

https://code.google.com/codejam/contest/6254486/dashboard#s=p1
"""

from string import maketrans


def evaluate_case(pancakes):
	"""Evaluates one case of the problem

	Transform +- to 10 for easy handling and start making maneuvers until all
	pankes are with the "happy" side up
	"""
	intab = '+-'
	outtab = '10'
	pancakes = pancakes.translate(maketrans(intab, outtab))
	faces = '10'
	moves = 0

	while True:
		face = str(faces.index(pancakes[0]))
		try:
			i = pancakes.index(face)
			pancakes = i*face + pancakes[i:]
			moves += 1
		except ValueError:
			if pancakes[0] == '0':
				moves += 1
			break
	return moves


def main():
	"""Main function
	
	Read the number of cases and the pancake stack
	"""
	t = int(raw_input())
	for i in xrange(1, t + 1):
  		pancakes = str(raw_input())
  		print "Case #{}: {}".format(i, evaluate_case(pancakes))


if __name__ == "__main__":
	main()
