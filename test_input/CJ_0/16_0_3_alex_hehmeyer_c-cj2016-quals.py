########################################################
# COIN JAM - Google Code Jam 2016 Quals
# Problem C
########################################################

import time

#########################
# GLOBAL VARIABLES
# A few global variables
#########################
# User Controlled Global Variables
SHOW_PERF_TIMES = False
SHOW_DEBUG = False

# Other Global Variables


#####################################################
# FUNCTIONS
# This section contains any necessary functions
#####################################################


###############################################################
# Default comparison function for quicksort and binsearch
# Returns -1 if a < b, 1 if a > b and 0 if they are equal
def defaultCompareFunc(a,b):
    if a == b:
        return 0
    elif a < b:
        return -1
    elif a > b:
        return 1
    

###############################################################
# BINARY SEARCH
# Binary Search for value in mylist using comparefunc to compare values
# Returns position in mylist for the value, if found, else returns -1
# Of course, mylist must be sorted already
def binsearch(value,mylist,comparefunc=defaultCompareFunc):
    lenmylist = len(mylist)
    lowerbound = 0
    upperbound = lenmylist-1
    currentpos = int((lowerbound+upperbound+1)/2)
    while lowerbound <= currentpos <= upperbound:
        comparevalue = comparefunc(value, mylist[currentpos])
        if comparevalue == 0:
            return currentpos
        elif comparevalue == 1:
            # "value" is greater - search right side of list
            if currentpos == lenmylist-1:
                return -1
            lowerbound = currentpos+1
            currentpos = int((lowerbound+upperbound+1)/2)
        else:
            # "value" is smaller - search left side of list
            if currentpos == 0:
                return -1
            upperbound = currentpos - 1
            currentpos = int((lowerbound+upperbound+1)/2)
    return -1


###############################################################
# This function requires that all primes less than or equal to the square root of n already be generated
# Also - assumes the list of primes is sorted
def isprimeN(n,PRIMES):
    numprimes = len(PRIMES)
    if PRIMES[numprimes-1] >= n:
        # We've actually already computed all primes to this point - just find and return it
        foundvalue = binsearch(n,PRIMES)
        if foundvalue >= 0:
            return True
        else:
            return False
    else:
        # We have not computed all primes to the number n yet, so must check up to it's sq root
        rootn = n ** 0.5
        i = 0
        while i < numprimes and PRIMES[i] <= rootn:
            if n%PRIMES[i] == 0:
                return False
            i += 1
    return True

# Generates list of all prime numbers up to and including n
# Reuses any previously computed primes
def generateprimestoN(n,PRIMES=[]):
    numprimes = len(PRIMES)
    if numprimes < 7:
        PRIMES = [2,3,5,7,11,13,17]
        numprimes = 7
    currentprime = PRIMES[numprimes-1]
    currentnum=currentprime+2
    while currentnum <= n:
        if isprimeN(currentnum,PRIMES):
            PRIMES.append(currentnum)
        currentnum += 2
    return PRIMES


# Returns all the prime factors of a number, N
# (excluding 1)
def findPrimeFactors(n,PRIMES=[]):
    numprimes = len(PRIMES)
    n = int(n)
    allfactors = []
    rootn = n ** 0.5

    if numprimes <= 0:
        PRIMES = generateprimestoN(rootn,PRIMES)
        numprimes = len(PRIMES)

    if rootn > PRIMES[numprimes-1]:
        PRIMES = generateprimestoN(rootn,PRIMES)
    
    i = 0
    while i < numprimes and PRIMES[i] <= rootn:
        if n%PRIMES[i] == 0:
            allfactors.append(PRIMES[i])
            allfactors.append(int(n/PRIMES[i]))
        i += 1

    if len(allfactors) == 0: # number is prime
        allfactors.append(n)
        
    return allfactors, PRIMES



# Changes binary number into base b
def changeBase(num, b):
    curval = num
    position = 0
    result = 0
    while curval > 0:
        if curval & 1 == 1:
            result += b**position
        position += 1
        curval >>= 1

    return result



#####################################################
# MAIN PROGRAM
#####################################################

verystart = time.clock()

# Read number of test cases
testcase_count = int(input())
casesdone = 0
start = time.clock()
PRIMES = [2,3,5,7,11,13,17]
# Main loop
while casesdone < testcase_count:
    casesdone += 1
    
    # Read the inputs for this test case here
    line = input()

    N, J = map(int, line.split(' '))

    # Echo the inputs for debugging
    if SHOW_DEBUG:
        print('\nCASE #' + str(casesdone) + ' N: ' + str(N) + ' J: ' + str(J))

    #####################
    # Start Solution Here
    #####################

    # The 1's on either end never change...this is the JAMSHELL
    JAMSHELL = 2**(N-1) + 1
    JAMSHELL_BASE = [0 for x in range(11)]
    for base in range(2,11):
        JAMSHELL_BASE[base] = changeBase(JAMSHELL, base)

    num_coinjams = 0
    all_coinjams = []
    # Iterate through all possible N-2 bit numbers
    # EXCEPT 0 - avoids need to factor JAMSHELL (which is a big number)
    for jam_candidate_inside in range(1, (2**(N-2))-1):
        jam_candidate_inside_shifted = jam_candidate_inside << 1
        jam_candidate = jam_candidate_inside_shifted | JAMSHELL

        if SHOW_PERF_TIMES and jam_candidate_inside % 1000000 == 0:
            stop = time.clock()
            print('Evaluating number ' + str(jam_candidate) + ' TIME so far: ' + str(stop-start))

        # For each one, convert it to the 9 different
        # numbers represented by the bases 2 to 10
        # Then factor each of the 9 numbers and keep track of a factor
        isjam = True
        divisors = [0 for x in range(9)] # pos 0 is divisor base 2, pos 1 divisor base 3 etc.
        for base in range(2,11):
            # Only need to test the "inside" part (shifted) of the jam_candidate since if it and
            # the JAMSHELL have a common factor, then the candidate is not prime and has the same factor
            # NOTE: this approach WILL miss potential jam shell numbers - but as long as we can find J
            # for a given N, we are fine.  Easy to test that for N = 16 and 32 we can get 50 and 500 respectively.
            # Advantage of this approach is we start by factoring very small numbers and just keep working
            # up until we simply find ANY non-prime in all bases.  Once we find J non-primes in all bases,
            # we are finished.  It runs very fast!
            inside_test_num = changeBase(jam_candidate_inside_shifted, base)
            factors, PRIMES = findPrimeFactors(inside_test_num,PRIMES)
            
            # check whether the factors divide the JAMSHELL in this base
            # If ANY of them do, we are set - keep track of that factor!
            isjam_inbase = False
            for factor in factors:
                if JAMSHELL_BASE[base] % factor == 0:
                    isjam_inbase = True
                    divisors[base-2] = factor
                    break

            if not isjam_inbase:
                isjam = False
                break
                       
        # If a number is not prime in any base, it is a coin jam number
        # Add it to our growing list of coin jam numbers with their divisors
        # and once we have J such numbers, we are done
        if isjam:
            # Add this number to the jam candidate list
            if SHOW_DEBUG:
                print(str(jam_candidate) + ' IS a coin jam number!' +
                      '\nFactors per base are: ' + str(divisors))

            all_coinjams.append((jam_candidate,divisors))
            num_coinjams += 1
            if num_coinjams >= J:
                break



    #############################
    # Solve and print the answer!
    #############################
    print('Case #' + str(casesdone) + ': ')
    for coinjam in all_coinjams:
        jamnumber = changeBase(coinjam[0],10)
        allfactors = ''
        for factor in coinjam[1]:
            allfactors += str(factor) + ' '
        allfactors = allfactors.rstrip()
        print(str(jamnumber) + ' ' + allfactors)

    if SHOW_DEBUG:
        print('TOTAL COINJAMS FOUND: ' + str(len(all_coinjams)))

    #############################
    # Some code to print out the script's performance, if that option is enabled
    if SHOW_PERF_TIMES and casesdone % 10 == 0:
        stop = time.clock()
        print('TIME:  Cases ' + str(casesdone-10) + ' to ' + str(casesdone) + ' TOTAL: ' + str(stop-start) + ' AVG: ' + str((stop-start)/10))
        start = time.clock()

veryend = time.clock()
if SHOW_PERF_TIMES:
    print('\nTIME:  Total Program Time: ' + str(veryend-verystart))
