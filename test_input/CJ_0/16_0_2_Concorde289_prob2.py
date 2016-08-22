__author__ = 'Austin'

# 2016 qualifier problem 2

# main method
f_in = open('p2.txt')
noOfTestCases = int(f_in.readline())
f_out = open('p2_out.txt', 'w')
for t in range(0, noOfTestCases):
    input_str = f_in.readline().strip()
    output = 0

    for i in range(1, len(input_str)):
        if input_str[i] != input_str[i-1]:
            output += 1
    if input_str[-1] == '-':
        output += 1

    # write to file
    f_out.write('Case #'+str(t+1)+": "+str(output)+"\n")

# close files
f_in.close()
f_out.close()
