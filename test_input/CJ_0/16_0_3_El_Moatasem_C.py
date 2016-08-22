'''
Created on Mar 19, 2016

@author: elmoatasem
'''



# import itertools
# def findsubsets(S,m):
#     return set(itertools.combinations(S, m))
# 
# 
# def get_jim_coins(N,J):
#     for i in
#      
# 
# 
# def get_all_cases(n,i,coinList,coinString):
#     if(i == n):
#         coinString.
#         ret
#     for i in range(n):


import itertools
import math

def generateCases(N,J):
    productList =  list(itertools.product(('0','1'), repeat=N))
    productListStrings = []
    for i in range(len(productList)):
        pattern = "".join(productList[i])
        productListStrings.append(pattern)
    return productListStrings



def solve_problem(N,J):
    cases = generateCases(N,J)
    selectedCases = []
    for i in range(len(cases)):
        caseList = list(cases[i])
        if(caseList[0] == '1' and caseList[N - 1] == '1' ):
            baseList = get_numbers_in_decimal (cases[i])
#             print  baseList
            divisorsList = []
            for k in range(len(baseList)):
                divisors = get_divisors(baseList[k])
                if(len(divisors) == 0):
                    divisorsList = []
                    break
                else :
                    divisorsList.append(divisors[len(divisors) - 1])
            if(len(divisorsList) <> 0):
                divisorsList.insert(0, int(cases[i]))
                selectedCases.append(divisorsList)
                print divisorsList
                if(len(selectedCases) == J):
                    break
                
    print selectedCases
    return selectedCases


def get_divisors(number):
    length = int(math.ceil(math.sqrt(number) + 1))
#     print length
    divisors = {}
    for i in range(2,length):
        if(number % i == 0):
            if(divisors.get(i) == None):
                divisors[i] = 1
            if(divisors.get(number / i) == None):
                divisors[number / i] = 1
    return divisors.keys()



def get_numbers_in_decimal (numberString):
    numberList = list(numberString[::-1])
    result = []
    for j in range(2,11):
        baseResult = 0
        for i in range(len(numberList)):
            baseResult += int(numberList[i])* (j**i)
        result.append(baseResult)
    return result
        

def format_result(result):
    for i in range(len(result)):
        result[i] = map(str, result[i])
        result[i] = ' '.join(result[i])
    return '\n'.join(result)



f_r = open('C.in',"r")
n_test=int(f_r.readline().strip()) 
f_w = open("C.out", "w")
result = ""
for i in range(n_test):
    N,J =  map(int,f_r.readline().split())
#     print generateCases(N,J)
    result = solve_problem(N,J)
#     print get_numbers_in_decimal ('1001')
#     print sorted(get_divisors(11))

    result = format_result(result)
    print result
    
    output_str='Case #{itr}: {res}'.format(itr=(i+1),res="\n"+result)
    f_w.write(output_str+'\n')
    
f_r.close()

