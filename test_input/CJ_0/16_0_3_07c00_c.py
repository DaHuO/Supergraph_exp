#!/usr/bin/env python

import sys
import commands

def addb(x, L):
	r = bin(int(x, 2) + 1)[2:]
	while len(r) < L:
		r = "0" + r
	return r

def get_each_base(x):
	r = []
	for i in range(2, 11):
		r.append(int(x, i))
	return r

def is_prime(q):
	q = abs(q)
	if q == 2:
		return True
	if q < 2 or q & 1 == 0:
		return False
	return pow(2, q-1, q) == 1

def devdev2(n):
	r = commands.getoutput("gfactor " + str(n))
	x = r.split()
	return [int(x[1])]

def devdev(n):
	i = 2
	table = []
	q = n
	print n
	while i * i <= n:
		while n % i == 0:
			n /= i
			table.append(i)
			if i != q:
				return table
		i += 1
	if n > 1:
		table.append(n)
	return table

def main():
	N = int(raw_input())
	for i in range(N):
		(n, j) = raw_input().split()
		n = int(n)
		j = int(j)
		x = addb("0", n-2)
		x = "1" + x + "1"
		print "Case #%d:" % (i+1)
		while 1:
			x = addb(x[1:n-1], n-2)
			x = "1" + x + "1"
			h = get_each_base(x)
			z = []
			r = None
			#print h
			for v in h:
				#print v,
				r = is_prime(v)
				if r == True:
					break
				t = devdev2(v)
				z.append(t[0])
			if r != True:
				print x, 
				for u in z:
					print u,
				print
				j -= 1
				if j == 0:
					break
		
if __name__ == '__main__':
	main()
