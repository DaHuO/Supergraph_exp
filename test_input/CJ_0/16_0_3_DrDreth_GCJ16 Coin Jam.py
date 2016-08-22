import math

def get_input( f = lambda x: x ):
    return map( f, raw_input( "Enter input:\n" ).splitlines()[1::] )

def get_file_input( fname, fn = lambda x: x ):
    with open( "D:\\Python Projects\\Google Code Jam Inputs\\" + fname ) as f:
        data = map( fn, f.readlines()[1::] )
    return data

def output_to_file( fname, inData ):
    inData.reverse()
    ind = 0
    with open( "D:\\Python Projects\\Google Code Jam Outputs\\" + fname, "w" ) as f:
        while inData:
            ind += 1
            f.write( "Case #" + str( ind ) + ": " + str( inData.pop() ) + "\n" )

def output_to_console( indata ):
    for i in xrange( len( indata) ):
        print "case #" + str( i + 1 ) + ": " + str( indata[ i ] )

inFname = "CJ.in"
outFname = "CJ.out"

data = get_input()
results = []

def check_prime( num ):
    #for i in xrange( 2, int( math.floor( float( num ) / 2.0 ) ) + 1 ):
    for i in xrange( 2, int( math.sqrt( num ) + 1 ) ):
        if num % i == 0:
            return [ False, i ]
    return [ True, -1 ]

for i in data:
    [ N, J ] = map( lambda x: int( x ), i.split() )
    low = 2 ** ( N-1 ) + 1
    high = 0
    for num in xrange( N ):
        high += 2 ** num
    bases = range( 2, 11 )
    for num in xrange( low, high, 2 ):
        binary = bin( num )[2::]
        flag = False
        divisors = []
        for base in bases:
            temp = int( binary, base )
            [ check, divisor ] = check_prime( temp )
            divisors.append( divisor )
            if check:
                flag = True
                break
        if not flag:
            results.append( [ binary, divisors ] )
            J -= 1
        if J == 0:
            break

print( "Case #1:" )
for i in results:
    string = i[ 0 ]
    for j in i[ 1 ]:
        string += " " + str( j )
    print string