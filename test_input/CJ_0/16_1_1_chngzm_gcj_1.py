repeat = int(input())
parameters = []
for i in range(repeat):
    new_input = input()
    parameters.append(new_input)
for i in range(len(parameters)):
    string_array = []
    for l in parameters[i]:
        string_array.append(l)
    new_array = [string_array[0]]
    for j in range(1,len(parameters[i])):
        if string_array[j] >= new_array[0]:
            new_array = [string_array[j]] + new_array
        else:
            new_array.append(string_array[j])
        string_array[j] = None
    print ("Case #{0}: ".format(i+1), end='')
    for z in new_array:
        print(z, end = '')
    print()
