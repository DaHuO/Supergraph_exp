import itertools
import random
import math
from fractions import gcd

from functools import reduce
from math import sqrt

_mrpt_num_trials = 5


def get_jamcoins(n, j):
	result_list = []

	for binary in itertools.product(["0", "1"], repeat=(n - 2)):
		b = "1" + "".join(binary) + "1"
		jamcoin = get_jamcoin(b)
		if jamcoin == None:
			continue
		else:
			result_list.append("{} {}".format(b, " ".join(jamcoin)))
			if len(result_list) == j:
				return result_list


def get_jamcoin(b):
	trivial_list = []
	for i in range(2, 11):
		con_num = int(b, i)
		if is_probable_prime(con_num):
			return None
		else:
			trivial = get_divisor(con_num)
			trivial_list.append(str(trivial))

	return trivial_list


def get_divisor(N):
	if N%2==0:
		return 2
	y,c,m = random.randint(1, N-1),random.randint(1, N-1),random.randint(1, N-1)
	g,r,q = 1,1,1
	while g==1:
		x = y
		for i in range(r):
			y = ((y*y)%N+c)%N
		k = 0
		while (k<r and g==1):
			ys = y
			for i in range(min(m,r-k)):
				y = ((y*y)%N+c)%N
				q = q*(abs(x-y))%N
			g = gcd(q,N)
			k = k + m
		r = r*2
	if g==N:
		while True:
			ys = ((ys*ys)%N+c)%N
			g = gcd(abs(x-ys),N)
			if g>1:
				break
	return g


def is_probable_prime(n):
	assert n >= 2
	if n == 2:
		return True
	if n % 2 == 0:
		return False
	# write n-1 as 2**s * d
	# repeatedly try to divide n-1 by 2
	s = 0
	d = n - 1
	while True:
		quotient, remainder = divmod(d, 2)
		if remainder == 1:
			break
		s += 1
		d = quotient
	assert (2 ** s * d == n - 1)

	# test the base a to see whether it is a witness for the compositeness of n
	def try_composite(a):
		if pow(a, d, n) == 1:
			return False
		for i in range(s):
			if pow(a, 2 ** i * d, n) == n - 1:
				return False
		return True  # n is definitely composite

	for i in range(_mrpt_num_trials):
		a = random.randrange(2, n)
		if try_composite(a):
			return False

	return True


t = int(input())

for i in range(1, t + 1):
	n, j = [int(s) for s in input().split(" ")]
	print("Case #{}:".format(i))
	for list in get_jamcoins(n, j):
		print(list)
