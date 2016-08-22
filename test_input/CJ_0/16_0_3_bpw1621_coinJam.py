#!/usr/bin/env python

from __future__ import print_function

import itertools
import math


class CoinJam( object ):
    def __init__( self, inputFile, outputFile ):
        self.inputFile = inputFile
        self.outputFile = outputFile
        self.jamCoins = []

        with open( inputFile, 'r' ) as i, open( outputFile, 'w+' ) as o:
            inputFileContents = i.readlines()
            numberOfCases = inputFileContents[ 0 ]
            inputFileContents[ 1 ]
            self.N, self.J = map( int, inputFileContents[ 1 ].split() )

            self.calculateJamCoins()
            self.printJamCoins( o )

    def calculateJamCoins( self ):
        for cartProd in itertools.product( ( '0', '1' ), repeat = self.N - 2 ):
            cartProdInnerString = ''.join( cartProd )
            cartProdString = '1' + cartProdInnerString + '1'
            baseReps = []
            for base in xrange( 2, 11 ):
                baseRep = int( cartProdString, base = base )
                baseReps.append( baseRep )

            nontrivialDivisors = map( CoinJam.isPrime, baseReps )
            if all( map( lambda x: x != 0, nontrivialDivisors ) ):
                self.jamCoins.append( ( cartProdString, baseReps, nontrivialDivisors ) )
                print( 'FOUND JAMCOIN #' + str( len( self.jamCoins ) ) )
            else:
                print( cartProdString + ' is not a jamcoin' )

            if len( self.jamCoins ) == self.J:
                return

            #print( cartProdString + ' : ' + str( zip( baseReps, nontrivialDivisors ) ) )

    @staticmethod
    def isPrime( number ):
        print( 'isPrime( ' + str( number ) + ' )' )
        if number % 2 == 0 and number > 2:
            return 2
        for i in xrange( 3, int( math.sqrt( number ) ) + 1, 2 ):
            print( str( number ) + ' / ' + str( i ) )
            if ( number % i ) == 0:
                return i

        return 0

    def printJamCoins( self, outputFile ):
        print( 'Case #1:', file = outputFile )
        for jamCoin in self.jamCoins:
            print( jamCoin[ 0 ] + ' ' + ' '.join( map( str, jamCoin[ 2 ] ) ), file = outputFile )
            #print( jamCoin[ 0 ] + ': ' + ' '.join( map( str, zip( jamCoin[ 1 ], jamCoin[ 2 ] ) ) ) )


if __name__ == '__main__':
    #coinJam = CoinJam( 'testInput.txt', 'results.txt' )
    #coinJam = CoinJam( 'C-small-attempt0.in', 'results-small.txt' )
    #coinJam = CoinJam( 'C-large.in', 'results-large.txt' )
    coinJam = CoinJam( 'C-large.in', 'test.txt' )

