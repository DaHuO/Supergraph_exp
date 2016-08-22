def not_prime(number):
    if number % 2 == 0:
        return (2)
    #limit the search to 100 to reduce time, otherwise a ridiculous amount of time will be spent 
    for i in range(3, 100, 2):
        if number % i == 0:
            return (i)
    return False
#only one test case so no need to repeat
repeat = int(input())
parameters = input().split()
repeat = 0
print("Case #1: ")
#repeat program for number of outputs needed

for j in range(2**(int(parameters[0])-2)):
    #finds the value in the middle of the first and last digit
    centre_number = bin(j)[2:]
    #add zeros to the front of the centre number
    for p in range(len(centre_number), int(parameters[0]) -2):
        centre_number = "0" + centre_number
    #add the first and last digit, which are one to get the new number
    number = "1" + centre_number + "1"
    divisor_array = []
    #get the different value for the different bases and check if all are not prime
    for q in range(2,11):
        current_number = 0
        for k in range(1, len(number) +1):
            current_number += (q ** (k-1)) * int(number[-k])
        number_divisor = not_prime(current_number)
        if number_divisor:
            divisor_array += [number_divisor]
        else:
            break
    if len(divisor_array) == 9:
        print (str(number), end =' ')
        for z in divisor_array:
            print (z, end = ' ')
        print ()
        repeat += 1
    if repeat == int(parameters[1]):
        break
