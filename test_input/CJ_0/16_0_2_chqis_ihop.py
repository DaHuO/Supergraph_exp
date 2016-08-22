import sys

def flip(n, pancakes):
    if n == -1: return
    temp = [None]*(n+1)

    # deep copy
    for i in range(n+1):
        temp[i] = pancakes[i]
    
    for i in range(n+1):
        if temp[i] == '+':
            pancakes[n-i] = '-'
        else:
            pancakes[n-i] = '+'

# gives index of first blank pancake or -1 if all are happy
def checkEnd(pancakes):
    for i in range(len(pancakes)-1, -2, -1):
        if i == -1: return i
        if pancakes[i] == '-':
            return i

def printResult(testCase, n):
    print("Case #"+str(testCase)+": "+str(n))
    
def main():
    T = int(sys.stdin.readline())
    for testCase in range(1,T+1):
        pancakes = list(sys.stdin.readline())[:-1] # remove \n
        end = checkEnd(pancakes)
        n = 0
        if end == -1:
            printResult(testCase, n)
            continue

        i = 0;
        while(end != -1):
            i=0
            x = pancakes[0]
            # find as many happy on the top as possible and flip them
            while (x == '+'):
                i+=1
                x = pancakes[i]
            if i != 0:
                flip(i-1, pancakes)
                n+=1

            end = checkEnd(pancakes)
            flip(end, pancakes)    
            n+=1
            end = checkEnd(pancakes)
        printResult(testCase, n)

main()
