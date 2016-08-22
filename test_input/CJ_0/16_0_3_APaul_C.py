#!/env/local/bin/python

import itertools

# another verification function for testing
def run():
    while True:
        try:
            verify( raw_input() )
        except KeyboardInterrupt:
            print "heh weak"
            return

# Verification function for testing
def verify(n):
    n = str(n)
    reps = [ change(n, i) for i in range(2,11) ]
    divs = [ find_divisor(r) for r in reps ]
    print zip(reps, divs)

# Changes the string number st to base base (returns an int)
def change(st, base):
    b = 1
    fin = 0
    for c in reversed(st):
        fin += b * int(c)
        b *= base
    return fin

# Returns the divisors of n if it is a jamcoin
# Returns false if it's not a jamcoin
# Takes: n is a string
def check(n):
    if n[0] == '0' or n[-1] == '0':
        return False
    reps = [ change(n, i) for i in range(2,11) ]
    divs = [ find_divisor(r) for r in reps ]
    if not divs.__contains__(1):
        return divs     # return the divisors of n (in bases 2 to 10 inclusive)
    else:               # if there are no divisors return False
        return False

def find_divisor(num):
    if num % 2 == 0:
            return 2
    if num % 3 == 0:
            return 3
    # Count by 6 to reduce run time
    # Be careful this loop will still take a while
    for i in range(6, int(num**0.5)+2, 6):
        if num % (i-1) == 0:
            return i-1
        if num % (i+1) == 0:
            return i+1
    return 1

# Takes a generator expression from main and returns the first 50 jamcoins
def output(g):
    try:
        outs = ["Case #1:"]
        while len(outs) < 51:
            try:
                n = next(g)
            except:
                outs[0] += " (Exception)"
                #return outs
                f = open("c-writer.txt","w")
                for o in outs:
                    f.write(o + '\n')
                return outs
            q = check(n)
            if q:
                ostring = n
                for div in q:
                    ostring += " " + str(div)
                outs.append(ostring)
    except KeyboardInterrupt:
        f = open("c-large.txt","w")
        for o in outs:
            f.write(o + '\n')
    return outs

def main():
    g = ( ''.join(str(x) for x in p) for p in itertools.product([0,1], repeat= int(raw_input()) ) )
#    g = ( ''.join(str(x) for x in p) for p in itertools.product([0,1], repeat=16) )
#    g = ( ''.join(str(x) for x in p) for p in itertools.product([0,1], repeat=32) )
    for o in output(g):
        print o

if __name__ == "__main__":
    main()
