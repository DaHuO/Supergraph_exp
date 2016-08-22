#!/usr/bin/python

import math
import itertools

txt = open("C-large.in", "r")

out = open("a.txt", "w")
list = []
case = 0
iter = itertools.count()


		
def is_prime(n):
  if n == 2 or n == 3: return -1
  if n < 2 or n%2 == 0: return 2
  if n < 9: return -1
  if n%3 == 0: return 3
  r = 20000
  f = 5
  while f <= r:
    if n%f == 0: return f
    if n%(f+2) == 0: return f+2
    f +=6
  return -1
  

for k in range(int(txt.readline().strip())):
	for i in txt:
		case = case + 1
		counter = 0
		i = i.split(' ')
		out.write("Case #"+  str(case) + ":\n")
		for num in iter:
			number = "%030d" % (int(bin(num)[2:]),)
			number = '1' + number + '1'
			for base in range(2,11):
				z = is_prime(reduce(lambda x, y: x*base + y, map(int, str(number))))
				if z != -1:
					list.append(z)
				else :
					list = []
					break
			if len(list) == 9:
				out.write(number + ' ')
				for aoua in range(9):
					out.write("" + str(list[aoua]) + " ")
				out.write('\n')
				list = []
				counter = counter + 1
			if counter == 500:
				exit(0)
		
		