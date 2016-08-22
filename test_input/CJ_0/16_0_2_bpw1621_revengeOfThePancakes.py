#!/usr/bin/env python

from __future__ import print_function


class RotP( object ):
    def __init__( self, inputFile, outputFile ):
        self.inputFile = inputFile
        self.outputFile = outputFile
        self.flipCounts = []

        with open( inputFile, 'r' ) as i, open( outputFile, 'w+' ) as o:
            inputFileContents = i.readlines()
            numberOfCases = inputFileContents[ 0 ]
            for case in inputFileContents[ 1: ]:
                self.determineFlips( list( case.rstrip() ) )
            self.printFlips( o )

    def determineFlips( self, case ):
        counter = 0
        flips = 0

        while( True ):
            print( str( counter ) + ': ' + ''.join( case ) )
            case = RotP.removeTrailingPluses( case )
            print( '    rem:        ' + ''.join( case ) )

            if not case:
                break
            elif case[ 0 ] == '-':
                case = RotP.flipAndReverse( case )
                flips += 1
            elif case[ 0 ] == '+':
                lastLeadingPlusIndex = -1
                searchForLeadingPluses = re.search( '^\++', ''.join( case ) )
                if searchForLeadingPluses:
                    lastLeadingPlusIndex = searchForLeadingPluses.end()
                beginningCase = case[ :lastLeadingPlusIndex ]
                endingCase = case[ lastLeadingPlusIndex: ]
                beginningCase = RotP.flipAndReverse( beginningCase, endingCase )
                case = beginningCase + endingCase
                flips += 1

            print( '    end:        ' + ''.join( case ) )
            counter += 1

        self.flipCounts.append( flips )

    @staticmethod
    def removeTrailingPluses( case ):
        return list( re.sub( r'\++$', '', ''.join( case ) ) )

    @staticmethod
    def flipAndReverse( case, tail = [] ):
        case = case[ ::-1 ]

        print( '    reverse:    ' + ''.join( case ) + ''.join( tail ) )

        for index, c in enumerate( case ):
            if c == '+':
                case[ index ] = '-'
            elif c == '-':
                case[ index ] = '+'

        print( '    flip:       ' + ''.join( case ) + ''.join( tail ) )

        return case

    def printFlips( self, outputFile ):
        for caseNumber, digitCount in enumerate( self.flipCounts ):
            print( 'Case #' + str( caseNumber + 1 ) + ': ' + str( digitCount ), file = outputFile )

if __name__ == '__main__':
    #rotp = RotP( 'testInput.txt', 'results.txt' )
    #rotp = RotP( 'myTestInput.txt', 'results.txt' )
    #rotp = RotP( 'B-small-attempt0.in', 'results-small.txt' )
    rotp = RotP( 'B-large.in', 'results-large.txt' )

