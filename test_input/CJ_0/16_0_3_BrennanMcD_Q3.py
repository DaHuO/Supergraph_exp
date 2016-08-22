#! /bin/bash/py
import random
import math

binaryList = []

def randomBinary(n):
	s = ""
	for i in range(n):
		s += "0" if random.random() > .5 else "1"
	return s

def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True  

def divisorGenerator(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            if i*i != n and i != 1:
            	return i
                



h = '''1
16 50'''

h = h.split('\n')

for case in range(int(h[0])):
	print("Case #" + str(case+1) + ": ")
	ite = 0
	while(ite != int(h[case+1].split(' ')[1])):
		binary = 0

		while(binary not in binaryList):
			binary = randomBinary(int(h[case+1].split(' ')[0]))
			binaryList.append(binary)
		jamCoin = True;
		for i in range(2,11):
			if is_prime(int(binary,i)):
				jamCoin = False;
		if jamCoin and str(binary)[-1] == "1" and str(binary)[0] == "1":
			print(binary, end=" ")
			for i in range(2,11):
				print(divisorGenerator(int(binary,i)),end=" ")
			print()


