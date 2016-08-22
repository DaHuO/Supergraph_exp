#!/bin/env python3

import sys
import os


def doChallenge(_input_filename):
	try:
		with open(_input_filename, 'r') as f:
			lines = f.read().split('\n')
	except FileNotFoundError:
		print("Input file '" + _input_filename + "' not found !")
		sys.exit()
	except PermissionError:
		print("Input file '" + _input_filename + "' could not be read !")
		sys.exit()
	except Exception:
		print("Unknown shit has happened")
		sys.exit()

	del lines[0] # First line is useless
	for i in range(len(list(filter(None, lines)))):
		S = lines[i]
		_ = ""
		for j in S:
			if len(_) == 0:
				_ = j
			elif _[0] <= j:
				_ = j + _
			else:
				_ = _ + j

		print("Case #" + str(i+1) + ': ' + _)



if __name__ == '__main__':
	try:
		sys.argv[1]
	except IndexError:
		print("Usage : " + sys.argv[0] + " filename")
	else:
		doChallenge(sys.argv[1])
