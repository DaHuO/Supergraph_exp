import sys, copy, math;

def findDivisor(value):
    #print(value)
    #print(math.sqrt(value))
    #print(int(math.sqrt(value)))
    #for i in range(2, int(math.sqrt(value)+1))):
    for i in range(2, min(int(math.sqrt(value)+1), 10000)):
        if value % i == 0:
            #print('value=',value,' i=',i)
            return i
    return 0
def convert(value, base):
    res = 0
    fac = 1
    while value > 0:
        #print(value)
        res+=(value & 1)*fac
        fac*=base
        value>>=1
    return res

def solve():
    rez = []
    for i in range(0, (1 << (n-2))-1):
        x = 1 << (n-1)
        x += i << 1
        x += 1
        
        #x = 1 << (n-1) + i << 1 + 1

        #print('i=',i,' x=',x);
        res = []
        d = findDivisor(x)
        #print('d=',d);
        if d == 0:
            continue
        res.append(d)
        #print(res)
        cantFindDivisor = False
        for j in range(3, 11):
            y = convert(x, j)
            #print('j=',j,' y=',y);
            d = findDivisor(y)
            #print('d=',d);
            if d == 0:
                cantFindDivisor = True
                break
            res.append(d)
        if cantFindDivisor:
            continue
        res.insert(0, y)
        print(len(res), ' ', res)
        rez.append(' '.join(str(x)for x in res));
        if len(rez) >= q:
            break
    return '\n'.join(str(x)for x in rez)

inputFile =  sys.argv[1] if (len(sys.argv) > 1) else "input.txt";
outputFile = sys.argv[2] if (len(sys.argv) > 2) else (inputFile + "out.txt") if (len(sys.argv) > 1) else "output.txt";
print( inputFile, outputFile)
file = open(outputFile, "w")

with open(inputFile, 'r') as f:
    t = int(f.readline())
    for i in range(1, t + 1):
        file.write("Case #" + str(i) + ": \n")
        n,q = map(int, f.readline().split())
        x = solve()
        file.write(str(x) + "\n")
file.close()            








