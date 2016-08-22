#! /usr/bin/env python3
'''
' Title:	Google Code Jam 2016 - C. Coin Jam
' Author:	Cheng-Shih, Wong
' Date:		2016/04/09
'''

from random import random
from random import uniform

prime = set()
isp = [True]*10**6
for i in range(2,10**6):
	if isp[i]:
		prime.add(i)
		for j in range(i+i,10**6,i): isp[i] = False

def isprime( val ):
	for p in prime:
		if p >= val: break
		if val%p == 0: return False, p
	return True, 0

def weighted_choice(choices):
	total = sum(w for c, w in choices)
	r = uniform(0,total)
	upto = 0
	for c, w in choices:
		if upto+w >= r: return c
		upto += w
	assert False, "Shoudn't get here"

def fitness(s):
	fit = 0
	for i in valr:
		if isprime( int(s,i) )[0]: fit += 1
	if s in sols: fit += 5
	return (fit, s)

def rdmgenerator():
	out = '1'
	for i in midr: out += '1' if random()>=0.5 else '0'
	out += '1'
	return out

def crossover(p,q):
	m = round(uniform(0,N-1))
	return p[:mid]+q[mid:], q[:mid]+p[mid:]

def mutation(u):
	if random()<0.05:
		k = round(uniform(1,N-2))
		u = u[:k]+('0' if u[k]=='1' else '1')+u[k+1:]
	return u

def nxtgen(preg):
	curg = []

	sumf = sum(f for f, p in preg)
	wpreg = [(p,sumf-f) for f, p in preg]
	for _ in hpplr:
		u = weighted_choice(wpreg)
		v = weighted_choice(wpreg)
		nu, nv = crossover(u,v)
		
		nu = mutation(nu)
		nv = mutation(nv)
		curg += [fitness(nu), fitness(nv)]
		print(curg)
	
	return sorted(curg)

def gen():
	ppl = set()

	for _ in pplr: ppl.add(fitness(rdmgenerator()))

	ppl = sorted( list(ppl) )

	while ppl[0][0]>0:
		ppl = nxtgen(ppl)
		print(ppl)
	
	for f, s in ppl:
		if len(sols)>=J or f>0: break
		sols.add(s)
	

T = int(input())
N, J = [int(v) for v in input().split()]
sols = set()
valr = range(2,11)
ppln = 20
pplr = range(ppln)
hpplr = range(ppln//2)
midr = range(1,N-1)

while len(sols)<J:
	#print(len(sols))
	gen()

print('Case #1:')
for s in sols:
	print(s,end='')
	for i in valr: print('', isprime(int(s,i))[1], end='')
	print('')
