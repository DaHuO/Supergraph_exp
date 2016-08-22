#
# Google Code Jam 2016
# Roaund 0: C. Coin Jam
# submission by EnTerr
#

'''

Input

The first line of the input gives the number of test cases, T. T test
cases follow; each consists of one line with two integers N and J.

Output

For each test case, output J+1 lines. The first line must consist of
only Case #x:, where x is the test case number (starting from 1). Each
of the last J lines must consist of a jamcoin of length N followed by
nine integers. The i-th of those nine integers (counting starting from
1) must be a nontrivial divisor of the jamcoin when the jamcoin is
interpreted in base i+1.

All of these jamcoins must be different. You cannot submit the same
jamcoin in two different lines, even if you use a different set of
divisors each time.

Limits

T = 1. (There will be only one test case.)
It is guaranteed that at least J distinct jamcoins of length N exist.

Small dataset: N = 16. J = 50.
Large dataset: N = 32. J = 500.


Input 
 	
Output 
 
1
6 3

Case #1:
100011 5 13 147 31 43 1121 73 77 629
111111 21 26 105 1302 217 1032 513 13286 10101
111001 3 88 5 1938 7 208 3 20 11


'''


import sys
from time import clock


f = open(sys.argv[1])
def input(): return f.readline().strip();

       
def print_minted_coinjams(n, j):
    '''
    observation - i notice it's a polynomial
    1x^15 + ? x^14 + ... ? x^1 + 1 x^0
    where we substitute 2..10 for x
    first and last coeficients = 1, rest unknown
    thought occurred, what if we design the polynom with a convenient divisor?
    (x^8 + 1) is convenient for n=16, shifts left by 8 by and adds the other divisor
    so the number will be divisor2 + divisor2 (concatenated as strings)
    we want 1st and last digit of divisor2 be 1, so we get n/2-2 bits of freedom
    turns out more than enough for small and large test cases
    '''
    # assuming even n
    n_free_bits = n//2 - 2
    div1 = '1' + '0' * n_free_bits + '01'
    for i in range(j):
        # 1 x y .. z t 1   of length n//2
        div2 = '1' + bin(i)[2:].rjust(n_free_bits, '0') + '1'
        coinjam = div2 + div2
        print coinjam,
        for k in range(2,11):
            print int(div1, k), 
            assert int(coinjam, k) % int(div1, k) == 0
        print
    return None
	

#clk = clock()

for caseNo in xrange(1, int(input())+1):
#    print >>sys.stderr, caseNo
    N, J = map(int, input().split())
    print 'Case #%d:' % caseNo
    print_minted_coinjams(N, J)
    
#print >>sys.stderr, 'time= %.1f seconds' % (clock()-clk )

