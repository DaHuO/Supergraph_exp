#!/usr/bin/env python3.2
#coding=UTF-8

'''

Google Code Jam 2016
Round 1a
Problem a
The Last Word

Instructions:
	chmod u+x process.py
	./process.py <input_file >output_file
	# stderr output is intended to display on a console

Notes:
	* it's not (necessarily) possible to produce any combination of the letters from S
	* number of combinations of choices: 2 ** (len(S) - 1)
		* do they all result in different words (aside from duplicate letters, at least)?
		* I think the answer is yes
		* approx. 2 ** len(S)
		* small dataset: 2 ** 14 = about 16k words
		* large dataset: 2 ** 1000 = super-big number
	* we want to quickly find the alphabetically last word, without enumerating the possibilities
	* the greatest letter should come first
		* this we can guarantee
		* when it comes to this letter, it is placed first, and all subsequent letters are placed after it (ie. in order)
		* for the letters beforehand, we should ensure that the greatest one in that collection comes first, and all subsequent ones after
		* seems we can do this with a recursive routine
	* 


'''

################################################################################


def read_case(id, input):
	S = input.readline().rstrip()
	return S

def greatest_index(S):
	index = 0
	for i in range(len(S)):
		if S[i] >= S[index]:
			index = i
	return index

def solution(S):
	if len(S) <= 1: return S
	index = greatest_index(S)
	inner = solution(S[0:index])
	return S[index] + inner + S[index+1:]

def solve_case(id, case):
	S = case
	return "Case #{}: {}\n".format(id, solution(S))



################################################################################


from sys import stdin, stdout, stderr
import time
import math
import pickle
import io

execution_timer = time.time
#execution_timer = time.clock
debugging = 1


################################################################################


def debug(message):
	if debugging:
		stderr.write(message() if hasattr(message, '__call__') else message)

def report(message):
	stderr.write(message)

def prepare_cached(prepare_data, pickle_path='data.pickle'):
	try:
		data = pickle.load(io.open(pickle_path, 'rb'))
		report("Loaded {}.\n".format(pickle_path))
	except IOError:
		data = prepare_data()
		report("Prepared {}.\n".format(pickle_path))
		pickle.dump(data, io.open(pickle_path, 'wb'))
	return data

def main():
	t0 = execution_timer()
	#prepare()
	t1 = execution_timer()
	report("Completed preparation in {:.6f} seconds.\n".format(t1 - t0))
	
	T = int(stdin.readline())
	for case_id in range(1,T+1):
		report("Processing test case {} of {} (output {}). {:.0f} seconds elapsed.".format(case_id, T, case_id-1, execution_timer() - t1))
		report("\n" if debugging else "\r")
		stderr.flush()
		stdout.write(solve_case(case_id, read_case(case_id, stdin)))
		stdout.flush()
	
	t2 = execution_timer()
	report("Processed {} test cases in {:.6f} seconds.                           \n".format(T, t2 - t1))
	report("Total time: {:.6f} seconds.\n".format(t2 - t0))


import sys
sys.setrecursionlimit(1010)



if __name__ == '__main__':
	main()

