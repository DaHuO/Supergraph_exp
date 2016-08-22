########################################################
#  - Google Code Jam 2016 Round 1a
# Problem A
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
    line = input()


    # Echo the inputs for debugging
    if SHOW_DEBUG:
        print('\nCASE #' + str(casesdone) + ' line: ' + line)

    #####################
    # Start Solution Here
    #####################

    sortedline = [line[0]]
    for i in range(1,len(line)):
        if line[i] >= sortedline[0]:
            sortedline = [line[i]] + sortedline
        else:
            sortedline =  sortedline + [line[i]]

    solution = ''
    for char in sortedline:
        solution += char



    #############################
    # Solve and print the answer!
    #############################
    print('Case #' + str(casesdone) + ': ' + solution)





    #############################
    # Some code to print out the script's performance, if that option is enabled
    if SHOW_PERF_TIMES and casesdone % 10 == 0:
        stop = time.clock()
        print('TIME:  Cases ' + str(casesdone-10) + ' to ' + str(casesdone) + ' TOTAL: ' + str(stop-start) + ' AVG: ' + str((stop-start)/10))
        start = time.clock()

veryend = time.clock()
if SHOW_PERF_TIMES:
    print('\nTIME:  Total Program Time: ' + str(veryend-verystart))
