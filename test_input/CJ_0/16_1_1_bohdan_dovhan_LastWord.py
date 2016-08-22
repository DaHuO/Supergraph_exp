import sys, copy;

def solve():
    ss = ''
    for c in s.split()[0]:
        #print(c)
        #print("ss[1]",ss[1])
        if ss != '':
            #print("ss[0]",ss[0])

            if c >= ss[0]:
                ss = c + ss
            else:
                ss = ss + c
        else:
            ss = c
        cc = c 
    return ss;

inputFile =  sys.argv[1] if (len(sys.argv) > 1) else "input.txt";
outputFile = sys.argv[2] if (len(sys.argv) > 2) else (inputFile + "out.txt") if (len(sys.argv) > 1) else "output.txt";
print(inputFile, outputFile)
file = open(outputFile, "w")

with open(inputFile, 'r') as f:
    t = int(f.readline())
    print(t)
    for i in range(1, t + 1):
        file.write("Case #" + str(i) + ": ")
        s = f.readline()
        file.write(str(solve()) + "\n")
file.close()            








