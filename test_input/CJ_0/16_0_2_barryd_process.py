#!/usr/bin/env python3.2
#coding=UTF-8

'''

Google Code Jam 2016
Round qualification
Problem b
Revenge of the Pancakes

Instructions:
	chmod u+x process.py
	./process.py <input_file >output_file
	# stderr output is intended to display on a console

Notes:
	* one way to be sure that we have the minimum number of flips, would be to consider all possible courses of action, at least up to the first confirmed solution
		* ie. a breadth-first search would do the job
		* but I don't think this is necessary at all
	* the stack of all + pancakes has no transitions between + and - in it
	* a flip eliminates a maximum of 1 transition? - yes, this seems quite clear
	* but even when the transitions are 0, 1 flip may still be required to switch ----- to +++++
	* can a flip be useful if it doesn't eliminate a transition?
		* if not, then each flip should always eliminate exactly 1 transition, making it easy to calculate the required flips
		* the case of flipping the final pancake is clearly an exception here
		* I suppose we could consider an implied final pancake which is happy - perhaps we put a happy face on the plates?
	* candidate solution:
		* flips_required = number_of_transitions + (1 if the final pancake is - else 0)


'''

################################################################################


def read_case(id, input):
	case = input.readline().rstrip()
	return case

def solution(stack):
	stack = stack + '+'
	transitions = 0
	for i in range(len(stack) - 1):
		if stack[i] != stack[i+1]:
			transitions += 1
	return transitions
	

def solve_case(id, case):
	return "Case #{}: {}\n".format(id, solution(case))


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

def main():
	t0 = execution_timer()
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

if __name__ == '__main__':
	main()

