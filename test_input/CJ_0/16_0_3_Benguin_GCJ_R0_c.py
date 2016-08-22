import math

def getDiv(n):
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return i
    return -1

def toBinary(n):
    return ''.join(str(1 & int(n) >> i) for i in range(16)[::-1])



fIn = open('input.txt', 'r')
fOut = open('output.txt', 'w')
case = 0
for line in fIn:
    case += 1
    if case > 1:
        print("Case"+str(case))
        n = int(line.split(' ')[0])
        j = int(line.split(' ')[1])
        fOut.write("Case #1:\n")
        start = int(str(1)+str(0)*(n-2)+str(1), 2)
        end = int(str(1)*n, 2)
        count = 0
        for i in range(start, end+1, 2):
            if count > 50:
                break
            isJam = True
            divs = []
            for b in range(2,11):
                num = 0
                for j in range(0,n):
                    num += int(str(toBinary(i))[n-j-1])*math.pow(b,j)
                div = getDiv(num)
                divs.append(str(div))
                if div == -1:
                    isJam = False
                    break
            if(isJam):
                count += 1
                print(count, str(toBinary(i))+" "+ ' '.join(divs)+"\n")
                fOut.write(str(toBinary(i))+" "+ ' '.join(divs)+"\n")
        