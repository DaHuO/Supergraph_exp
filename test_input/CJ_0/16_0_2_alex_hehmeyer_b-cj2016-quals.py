########################################################
# REVENGE OF THE PANCAKES - Google Code Jam 2016 Quals
# Problem B
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








#####################################################
# MAIN PROGRAM
#####################################################

verystart = time.clock()

# Read number of test cases
testcase_count = int(input())
casesdone = 0

# Main loop
start = time.clock()
while casesdone < testcase_count:
    casesdone += 1
    
    # Read the inputs for this test case here
    S = input().strip()


    # Echo the inputs for debugging
    if SHOW_DEBUG:
        print('\nCASE #' + str(casesdone) + '\nS: ' + str(S))

    #####################
    # Start Solution Here
    #####################

    # Count how many changes there are in the stack starting
    # from the left hand side
    currentchar = S[0]
    change_count = 0
    for char in S:
        if currentchar != char:
            currentchar = char
            change_count += 1

    # Add one if the last pancake is a '-'
    if S[-1] == '-':
        change_count += 1



    #############################
    # Solve and print the answer!
    #############################
    print('Case #' + str(casesdone) + ': ' + str(change_count))





    #############################
    # Some code to print out the script's performance, if that option is enabled
    if SHOW_PERF_TIMES and casesdone % 10 == 0:
        stop = time.clock()
        print('TIME:  Cases ' + str(casesdone-10) + ' to ' + str(casesdone) + ' TOTAL: ' + str(stop-start) + ' AVG: ' + str((stop-start)/10))
        start = time.clock()

veryend = time.clock()
if SHOW_PERF_TIMES:
    print('\nTIME:  Total Program Time: ' + str(veryend-verystart))
