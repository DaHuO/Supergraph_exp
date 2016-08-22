# Pancakes stuff
import sys

input_file = r"C:\Documents and Settings\Dell D610\My Documents\Code\GCJ\Round0\Prob2\input.txt"
output_file = r"C:\Documents and Settings\Dell D610\My Documents\Code\GCJ\Round0\Prob2\output.txt"
output = open( output_file, 'w')
input = list()
use_file = True
if use_file == True:
	file = open( input_file, 'r' )
	input = [line.rstrip() for line in file]
	file.close()
else:
	input = ( 3, "--+--+--+----+++-+--", "+++----+---++--+++++--++---++", "--+-++-+++-++---++-++++-+--+++--++---++-++---++++--++" )
	
def countStackFlips( input_stack ):
	state = input_stack[0]
	group_count = 1
	
	for pancake in input_stack:
		if pancake != state:
			group_count += 1
			state = pancake
	
	num_flips = group_count
	if state == '+':
		num_flips -= 1
	return num_flips
	
def solveProblem( input ):
	num_cases = input[0]
	input = input[1:]
	
	for index_case in range( 0, len( input ) ):
		num_flips = countStackFlips( input[index_case] )
		output.write( "Case #%d: %d\n" % ( index_case + 1, num_flips ) )
	
	output.close()

solveProblem( input )
		
	