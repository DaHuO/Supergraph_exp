### Set the input and output file names
import time
import datetime
filename = 'A-large'
input_filename = filename + '.in'
output_filename = filename + '.out.' + datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d-%H%M%S') + '.txt'


### Open input file for reading
with open(input_filename) as f:
    lines = f.read().splitlines()

    ### Open output file for writing
    with open(output_filename, 'w') as output:

        ######################################################
        ### Initialise variables from first line of the file
        ######################################################   
        vars = lines[0].split(' ')
        cases = int(vars[0])                    # number of cases
        print(str(cases) + ' cases detected.')  # [soft validation]
        lineNum = 1                             # first case starts here
        caseNum = 0                             # for counting the num of cases
        caseSize_r = 1                          # number of rows in each case; default = 1
        caseSize_c = 1                          # number of columns in each case; default = 1
        
        #infoLines = True                        # Toggle according to question
        infoLines = False                       # Toggle according to question
        
        ### i.e. infoLines == True
        if infoLines:
            print('skipped')
                
        ### i.e. infoLines == False
        else:   
            for caseNum in range(1, cases+1):
                
                ### Do the Work!
                ### TODO! 
                
                my_str = str(lines[lineNum].split(' ')[0])
                my_arr = list(my_str)
                
                myAns = ''
                n = 0
                for c in my_arr:
                    if n == 0:
                        myAns = my_arr[n]
                    else:
                        #print(myAns)
                        if myAns[0] <= my_arr[n]:
                            myAns = my_arr[n]+myAns
                        else:
                            myAns = myAns+my_arr[n]
                    n = n + 1
               
                ### Output myAns
                print('Case #%d: %s' % (caseNum, "".join(str(x) for x in myAns)))
                output.write('Case #%d: %s\n' % (caseNum, "".join(str(x) for x in myAns)))

                lineNum += 1
                

### END
