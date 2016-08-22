test_num = '1000000000000001'
number_of_case = 0
output_file = open("solution.txt", "w")
output_file.write("Case #1:\n") 
prove_base = [[0]*11 for i in range(50)]
index_prove_base = 0
complete = 0
def is_prime(test):
    for index in range(2, int(pow(test,0.5))):
        if test % index == 0:
            return index
    return 0
def is_complete(num_base):
    evidence = [0] * 11
    for i in range(2,11):
        evidence[i] = is_prime(num_base[i])
        if evidence[i] == 0:
            return 0
    return evidence

for i in range(100000000):
    all_base_num = [0] * 11
    for j in range(2,11):
        all_base_num[j] = int(test_num,j)
    evidence = is_complete(all_base_num)
    if(evidence != 0):
        prove_base[number_of_case][0] = test_num
        prove_base[number_of_case][2:11] = evidence[2:11]
        number_of_case += 1
        output_file.write(test_num + " ")
        output_file.write(" ".join([str(divisor) for divisor in evidence[2:11]]))
        output_file.write("\n")
    if number_of_case == 50:
        break
    test_num = int(test_num,2) + 2
    test_num = bin(test_num)[2:]
    test_num = str(test_num)
    
output_file.close()