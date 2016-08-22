from math import *
from itertools import accumulate

#input_file = open('A-sample.in','r')
#input_file = open('A-small-attempt0.in.txt','r')
input_file = open('A-large.in.txt','r')
raw_input = input_file.read()

lines = raw_input.split('\n')

num_cases = int(lines[0])
case_num = 1

output_text = ''
output_file = open('A.txt','w')

debug=0

###################

digits = [False]*10

while case_num<=num_cases:
    S=lines[case_num]
    
    output_text += ('Case #'+str(case_num)+': ')

    ans = S[0]
    for i in range(1,len(S)):
        if S[i]>=ans[0]:
            ans=S[i]+ans
        else:
            ans=ans+S[i]

    output_text += ans+'\n'
    case_num += 1


if debug: print('\n'+output_text)
output_file.write(output_text)
input_file.close()
output_file.close()
