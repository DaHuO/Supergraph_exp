from sys import argv
import math

def check_prime(val):
    sqrt_v = int(math.sqrt(val))
  
    for i in range (2, sqrt_v):
        if((val % i) == 0):
            return False, int(val / i)
            
    return True, None
    
script, in_file, out_file = argv
input = open(in_file)
content = input.read().splitlines()
input.close()

test_count = 0
test_cases = []
line_index = 0
index = 1

for line in content:
    if(line_index == 0):
        test_count = int(line)
    else:
        test_cases.append(line)
        
    line_index += 1
    
output = open(out_file, "wb")
for case in test_cases:
    stack = case.split(' ')
    leng = int(stack[0]) - 2
    desired = int(stack[1])
    actual = 0
    results = []
    for i in range(0, int(math.pow(2,leng))):
        coin_b = bin(i)[2:]
        for zerps in range(0, leng - len(coin_b)):
            coin_b = '0' + coin_b
        coin_b = '1' + coin_b + '1'
        
        non_trivial_list = []
        for intr in range(2, 11):
            coin_d = int(coin_b,intr)
            result, non_trivial_div = check_prime(coin_d)
            
            if(result == False):
                non_trivial_list.append(non_trivial_div)
            else:
                non_trivial_list = []
                break
        if(len(non_trivial_list) != 0):
            non_trivial_list.insert(0, coin_b)
            results.append(non_trivial_list)
            actual += 1
            print actual
            
        if(actual == desired):
            output.write("Case #" + str(index) + ": \n")
            for res_idx in range(0, desired):
                for x in range(0, 10):
                    output.write(str(results[res_idx][x]) + ' ')
                output.write("\n")
            index += 1
            break
output.close()
    
                