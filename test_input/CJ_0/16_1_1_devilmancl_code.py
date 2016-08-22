import sys
import copy
import math
from collections import deque

#obtain the name of the input
def fileName():
    filename = 'input'
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        print("File was not indicated")
        exit()
    return filename

fn = fileName()
file = open(fn, 'r')
out = open('output', 'w')

line_number = 1;
testcase = 1
max_testcases = 0
tc_ln = 0

while True:
    line = file.readline()
    if line:
        line = line.replace("\n","")
        inputs = line.split(" ")
        #how many test cases are
        if line_number == 1:
            max_testcases = int(inputs[0])
            line_number = 2
            tc_ln = 0
            continue

        S = inputs[0]
        R = deque()
        for i in range(len(S)):
            if len(R) == 0:
                R.append(S[i])
            else:
                for fR in R:
                    if S[i] >= fR:
                        R.appendleft(S[i])
                    else:
                        R.append(S[i])
                    break
            #print(R)
       
        out.write("Case #"+str(testcase)+": "+str(''.join(R))+"\n")
        out.flush()
        tc_ln = 0
        testcase = testcase + 1
        line_number += 1
    else:
        break
file.close()
out.close()
exit()