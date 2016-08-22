# -*- coding: utf-8 -*-
"""
Created on Fri Apr 08 19:06:53 2016

@author: caiyi
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Apr 08 19:06:53 2016

@author: caiyi
"""

"""
counting sheep
"""
def write_res(file_name, res):
    with open(file_name,'w') as f:
        res_str = ''
        for i in range(len(res[:-1])):
            res_str += "Case #{}: ".format(i+1)+ str(res[i])+'\n'
        res_str += "Case #{}: ".format(i+2) + str(res[-1])
        f.write(res_str)


def func(S):
    """
    S: a string contains '+' and '-'
    return the last number before sleep, if never stop, return INSOMNIA
    dont try to change S
    
    """
    
    L = len(S)
    if S == '+' * L:
        return 0
    if S == '-' * L:
        return 1
    
    if S[-1] =="+":
        right = L - 1
        while S[right] == '+':
            right -= 1
        return func(S[:right+1])
    else:
        left = 0
        if S[left] == '-':
            while S[left] == '-' and left < L:
                left += 1
            return 1 + func(''.join(['+' if l=='-' else '-' for l in S[left:]])[::-1]) # a shorter one
        else:
            while S[left] == '+' and left < L:
                left += 1
            return 1 + func('-'*left + S[left:]) # the saome length
            
#l = ['-','-+','+-','+++','--+-','---+','+++-','']
#for S in test_case:
#    print S
#    print func(S)
        
    
        
#        
with open('B-large.in') as f:
    str1 = f.read()
    l = [S for S in str1.strip().split('\n')[1:]]
    
res = []
for S in l:    
    #num = int(ch)
    print "the S", S
    
    tmp = func(S)
    print 'the result ', tmp
    #print tmp
    res.append(tmp)
    
write_res('res_B_large.txt', res)
        
    
    

    
    