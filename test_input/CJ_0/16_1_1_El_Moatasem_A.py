'''
Created on Mar 19, 2016

@author: elmoatasem
'''








def solve_problem(word):
    res = word[0]
    for i in range(1,len(word)):
        choices = sorted([res+word[i],word[i]+res],)
        res = choices[1]
    return res







f_r = open('A-large.in',"r")
n_test=int(f_r.readline().strip()) 
f_w = open("A.out", "w")
result = ""
for i in range(n_test):
    word =  f_r.readline().strip()
    result = solve_problem(word)
    print result
    output_str='Case #{itr}: {res}'.format(itr=(i+1),res=result)
    f_w.write(output_str+'\n')
    
f_r.close()
















