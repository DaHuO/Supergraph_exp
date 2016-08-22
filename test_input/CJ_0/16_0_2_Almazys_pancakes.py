#!/bin/env python3

import sys
import os
import re

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
		pancakes = lines[i]

		#Deleting duplicates in series (++++ -> + ; ---- -> -)
		p = re.compile('\++')
		pancakes = p.subn('+', pancakes)[0]
		p = re.compile('-+')
		pancakes = p.subn('-', pancakes)[0]

		if pancakes[-1] == '+':
			_ = list(pancakes)
			del(_[-1])
			pancakes = ''.join(_)

		#start counting
		res = 0

		p = re.compile('\+-')
		res = int(p.subn('', pancakes)[1]) * 2
		if len(pancakes)>0 and pancakes[0] == '-':
			res = res+1

		print("Case #" + str(i+1) + ": " + str(res))




if __name__ == '__main__':
	try:
		sys.argv[1]
	except IndexError:
		print("Usage : " + sys.argv[0] + " filename")
	else:
		doChallenge(sys.argv[1])
