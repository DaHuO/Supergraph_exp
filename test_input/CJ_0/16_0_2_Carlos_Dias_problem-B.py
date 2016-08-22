#!/usr/bin/python3

def plusUntilMinus( stack ):
	if ( stack[0] == '-' ):
		return len( stack )

	for i in range( 1, len( stack ) ):
		if ( stack[i] != '+' ):
			return i

	return len( stack )

def move( stack, i ):
	return ( stack[:i].replace( '-', 't' ).replace( '+', '-' ).replace( 't', '+' )[::-1] + stack[i:] )

def solve( stack, n = 0 ):
	stack   = stack.rstrip( '+' )
	
	if ( len( stack ) == 0 ):
		return n

	return solve( move( stack, plusUntilMinus( stack ) ), n + 1 )

def Main():

	for testCase in range( 1, int( input() ) + 1 ):
		stack = input()
		print( 'Case #{0}: {1}'.format( testCase, solve( stack ) ) )

# End Main

if __name__ == '__main__':
	Main()