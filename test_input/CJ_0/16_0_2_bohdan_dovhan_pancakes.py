import sys, copy, math;

def solve():
    rez = 0
    c = '+'
    print('s=',s)
 
    print('s r=',s.split()[0][::-1])
    for x in s.split()[0][::-1]:
        if x != c:
            c = x
            rez+=1
    print(rez)
    return rez

inputFile =  sys.argv[1] if (len(sys.argv) > 1) else "input.txt";
outputFile = sys.argv[2] if (len(sys.argv) > 2) else (inputFile + "out.txt") if (len(sys.argv) > 1) else "output.txt";
print( inputFile, outputFile)
file = open(outputFile, "w")

with open(inputFile, 'r') as f:
    t = int(f.readline())
    for i in range(1, t + 1):
        file.write("Case #" + str(i) + ": ")
        s = f.readline()
        x = solve()
        file.write(str(x) + "\n")
file.close()            








