#
# Google Code Jam 2016
# Roaund 0: D. Fractiles
# submission by EnTerr
#

'''

Input

The first line of the input gives the number of test cases, T. T test
cases follow. Each consists of one line with a string S.

Output

For each test case, output one line containing Case #x: y, where x is
the test case number (starting from 1) and y is the winning last word,
as described in the statement.

Limits

1 <= T <= 100.
Small dataset   1 <= length of S <= 15.
Large dataset   1 <= length of S <= 1000.


Input 
7
CAB
JAM
CODE
ABAAB
CABCBBABC
ABCABCABC
ZXCASDQWE

Output 
Case #1: CAB
Case #2: MJA
Case #3: OCDE
Case #4: BBAAA
Case #5: CCCABBBAB
Case #6: CCCBAABAB
Case #7: ZXCASDQWE


'''


import sys
from time import clock


f = open(sys.argv[1])
def input(): return f.readline().strip();

       
def lastWord(s):
    res = ''
    for c in s:
        if c + res > res + c:
            res = c + res
        else:
            res = res + c
    return res


#clk = clock()

for caseNo in xrange(1, int(input())+1):
    #print >>sys.stderr, caseNo
    s = input()     #.split()
    print 'Case #%d:' % caseNo, lastWord(s)
    
#print >>sys.stderr, 'time= %.1f seconds' % (clock()-clk )

