# File name
#input_file_name = "A-large-practice.in"
input_file_name = "B-small-attempt0.in"
output_file_name = input_file_name + '.out'

# Input input_file
input_file = open(input_file_name, 'r')
output_file = open(output_file_name, 'w')

# Total cases
case_number = int(input_file.readline())

# Deal with each case
for case_i in range(case_number):

    # Always do some formating after split
    line = input_file.readline()
    seq_str = line.strip()
    seq = []
    for i in range(len(seq_str)):
        if(seq_str[i] == '+'):
            seq.append(True)
        elif(seq_str[i] == '-'):
            seq.append(False)
    state = seq[0]
    cost = 0

    # Ensure all pancake in the same state
    for i in range(1, len(seq_str)):
        if seq[i] != state:
            cost = cost + 1
            state = seq[i]

    # Last flip
    if state == False:
        cost = cost + 1

    # Print
    output_file.write('Case #' + str(case_i + 1) + ': ' + str(cost) + '\n')

input_file.close()
output_file.close()
