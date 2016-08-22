import os
os.chdir('/Users/mac/OneDrive/competitions/codejam 2016/round2/last_word')

##extra_need

def getW(s):
    output = ''
    for x in s:
        if x+output > output+x:
            output = x+output
        else:
            output = output+x
    return output
            
        
    


##read test.in
test_f = open('./tests/A-large.in.txt')
out_f = open('./tests/A-large.out.txt', 'w+')
test_num = None
test_case_num = 1
for line in test_f:
    if test_num == None:
        test_num = int(line)
    else:
        s = line.strip()
        T = getW(s)
        #print '{}, {}, {}'.format(max_s, audiences, extra_need) 
        out_f.write('Case #{}: {}\n'.format(test_case_num, T))
        test_case_num += 1
        
test_f.close()
out_f.close()