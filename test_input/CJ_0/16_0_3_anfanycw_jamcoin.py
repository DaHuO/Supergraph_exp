#!/usr/bin/python
from __future__ import print_function
import math
import time

outfile = None
used_coins = {}
last_number = -1

def run():
	global outfile
	outfile = open("output.txt", "w")

	with open("input.txt", "r") as f:
		lines = []
		for line in f:
			lines.append(line.strip("\n"))

		lines = lines[1:]

		for i,l in enumerate(lines):
			params = l.split(" ")
			n = int(params[0])
			j = int(params[1])
			gimme_some_jamcoins(i+1, n, j)

def find_divisor(num):
	# fail case
	divisor = 0

	# positives
	num = abs(int(num))

	# crude but fast, skip em if it aint workin
	if num % 2 == 0:
		divisor = 2
	elif num % 3 == 0:
		divisor = 3
	elif num % 5 == 0:
		divisor = 5
	elif num % 7 == 0:
		divisor = 7
	elif num % 11 == 0:
		divisor = 11
	elif num % 13 == 0:
		divisor = 13
	elif num % 17 == 0:
		divisor = 17
	elif num % 19 == 0:
		divisor = 19
	elif num % 23 == 0:
		divisor = 23
	elif num % 29 == 0:
		divisor = 29
	elif num % 31 == 0:
		divisor = 31
	elif num % 37 == 0:
		divisor = 37

	return divisor

def create_divisor_list(value):
	divisors = []

	# set up dict with base values used to get divisors
	bases = dict.fromkeys([2,3,4,5,6,7,8,9,10])
	for k,v in bases.iteritems():
		base_rep = int(value, k)
		divisor = find_divisor(base_rep)
		if divisor > 0:
			divisors.append(divisor)
		else:
			return None
	return divisors

def get_value(length):
	global used_coins, last_number

	starting_num = int(math.pow(2, length-1) + 1)
	# only want odd numbers for first and last char of binary rep => '1'
	i = last_number if last_number > 0 else starting_num
	check = ''
	while True:
		check = bin(i)[2:]
		if len(check) == length:
			# make sure we don't use the same coin again
			if not used_coins.get(check):
				used_coins[check] = True
				break
		i += 2
	last_number = i
	return check

def create_jam_dict(size):
	arr_range = range(1,size+1)
	top = dict.fromkeys(arr_range)
	for k,v in top.iteritems():
		coins = dict.fromkeys(['coin', 'divisors'])
		top[k] = coins
	return top

def write_results(index, jamcoins):
	global outfile
	print("Case #%d:" % (index), file=outfile)
	for r,v in jamcoins.iteritems():
		line = "%s " % (v['coin'])
		line += " ".join(str(d) for d in v['divisors'])
		print("%s" % line, file=outfile)

def gimme_some_jamcoins(index, length, coins):
	global last_number

	# dict to hold results
	jamcoins = create_jam_dict(coins)

	found_divisors = True
	found = 0
	while found < coins:
		# get binary rep of a potential jamcoin
		bin_rep_value = get_value(length)

		# create the list of base values
		divisors = create_divisor_list(bin_rep_value)
		if divisors is None:
			continue

		# if here, we found a list of divisors
		found += 1
		jamcoins[found]['coin'] = bin_rep_value
		jamcoins[found]['divisors'] = divisors

	write_results(index, jamcoins)
	used_coins = {}
	last_number = -1

run()