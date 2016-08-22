#!/usr/bin/python3

from threading import Thread

def firstMultiple( number ):
	if ( number % 2 == 0 ):
		return 2

	for i in range( 3, int( number**0.5 ) + 1, 2 ):
		if ( number % i == 0 ):
			return i

	return False

def printFirstJamcoin( inferior, superior ):
	for x in range( inferior, superior, 2 ):
		multiples = []
		found     = True
		jamcoin   = '{0:b}'.format( x )

		for b in range( 2, 11 ):
			multiple = firstMultiple( int( jamcoin, base = b ) )

			if ( not multiple ):
				found = False
				break

			multiples.append( multiple )
		
		if( found ):
			print( jamcoin, *multiples )
			#return x

def Main():

	for testCase in range( 1, int( input() ) + 1 ):
		N, J = [ int( num ) for num in input().split() ]

		limiteInferior  = ( 2**( N - 1 ) )
		limiteSuperior  = ( 2**N )
		numberOfThreads = 256
		parcela         = ( limiteSuperior - limiteInferior )/numberOfThreads

		print( 'Case #{0}:'.format( testCase ) )

		for x in range( 0, numberOfThreads ):
			inicio = int( limiteInferior + x*parcela ) + 1
			fim    = int( inicio + parcela )
			Thread( target = printFirstJamcoin, args = ( inicio, fim ) ).start()
			
		# for x in range( 0, J ):
		# 	limiteInferior = printFirstJamcoin( limiteInferior, limiteSuperior ) + 2

# End Main

if __name__ == '__main__':
	Main()