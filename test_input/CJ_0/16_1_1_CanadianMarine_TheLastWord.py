# Round1A Problem A

def findLastWord( S ):
	word = ""
	
	for char in S:
		possible_choices = ( word + char, char + word )
		# Sort possible choices into alphabetical order, ascending
		# This will cause the choice of a lower alphabetical order to 'float' to the top
		possible_choices = sorted( possible_choices, reverse=True )
		word = possible_choices[0]
	
	return word
		
def testSorted( S ):
	return sorted( S, reverse=True )
	
if __name__ == '__main__':
	input_file_path = r"N:\Python Scripts\Round1\Prob0\input.txt"
	output_file_path = r"N:\Python Scripts\Round1\Prob0\output.txt"
	input_file = open( input_file_path, 'r' )
	output_file = open( output_file_path, 'w' )
	cases = input_file.readlines()[1:] # Skip the first line telling us the number of cases
	
	for case in range( 0, len( cases ) ):
		output_file.write( "Case #%d: %s" % ( case + 1, findLastWord( cases[case] ) ) )