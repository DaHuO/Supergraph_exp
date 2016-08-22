#get number of test cases
test_cases = int(input())
input_array = []
for i in range(test_cases):
    input_string = input()
    input_array.append(input_string)
#repeat process for each array element
for i in range(1,len(input_array)+1):
    current_pancake = input_array[i-1]
    new_pancake = ''
    flips = 0
    last_sad = 0
    while '-' in current_pancake:
        for j in range(len(current_pancake)):
            #finding position of the last negative
            if current_pancake[j] == '-':
                last_sad = j
        #flip the pancakes starting from the last negative one
        for k in range(last_sad+1):
            if current_pancake[k] == '-':
                new_pancake += '+'
            else:
                new_pancake += '-'
        new_pancake += current_pancake[last_sad+1:]
        #reverse nack to the original
        current_pancake = new_pancake
        new_pancake = ''
        #count number of flips
        flips += 1
    #print out the cases and the respective number of flips
    print ("Case #{0}: {1}".format(i, flips))
    
    
