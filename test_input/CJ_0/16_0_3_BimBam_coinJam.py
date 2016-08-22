import math

def binGen(d):
    if not d:
        yield '01'
        yield '11'
    else:
        for r in binGen( d - 1):
            yield '0'+ r
            yield '1'+ r
    return
        
def memo( f ):
    c = {}
    def mf( *args ):
        if args not in c:
            r = f( *args )
            c[args] = r
            return r
        else:
            return c[args]
    return mf

@memo
def divisor( x ):
    for d in range(2, int(math.sqrt(x)) + 2):
        if x % d == 0:
            return d
    return None

def divides( numbers ):
    r = []
    for n in numbers:
        tmpR = divisor( n )
        if tmpR is None:
            return (False, [])
        else:
            r.append( tmpR)
    return (True, r )

import sys
cnt = 0
print "Case #1:"
for index, x in enumerate(binGen(13)):
    if cnt == 50:
        break
    #y = '1'+sys.argv[1]+x
    y = '1'+x
    numbers = map( lambda yy: int(y, yy), range(2,11))
    good, divisors = divides(numbers)
    divisors = map(divisor, numbers)
    if good:
        cnt += 1
        print y, ' '.join( map(str, divisors) )
