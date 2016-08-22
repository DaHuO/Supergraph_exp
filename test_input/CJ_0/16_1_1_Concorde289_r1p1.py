__author__ = 'Austin'

# main method
f_in = open('p1.txt')
noOfTestCases = int(f_in.readline())
f_out = open('p1_out.txt', 'w')
for t in range(0, noOfTestCases):
    input_str = f_in.readline().strip()
    output = ""
    for c in input_str:
        if len(output) == 0:
            output = c
        elif c >= output[0]:
            output = c + output
        else:
            output += c

    # write to file
    f_out.write('Case #'+str(t+1)+": "+str(output)+"\n")

# close files
f_in.close()
f_out.close()
